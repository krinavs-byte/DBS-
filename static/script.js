// static/script.js
// Frontend dashboard behaviors (drag/drop, customize modal, save/load layout)
// Works with server-rendered Jinja variables when provided, falls back to localStorage when backend not present.

const DEV_LOCALSTORAGE_KEY = 'jodo_dashboard_layout_v1'

// Panel registry: available panels (id, title, description)
const PANEL_REGISTRY = [
  {id: 'stock_alerts', title: 'Stock Alerts', description: 'Items below threshold'},
  {id: 'transfers', title: 'Transfers', description: 'Pending transfers'},
  {id: 'kpi_strip', title: 'KPIs', description: 'High-level stats'},
  {id: 'recent_activity', title: 'Recent Activity', description: 'Latest actions'},
]

// Default layout: simple list with order
const DEFAULT_LAYOUT = [
  {id: 'kpi_strip', w:12,h:1},
  {id: 'stock_alerts', w:6,h:4},
  {id: 'transfers', w:6,h:4},
  {id: 'recent_activity', w:12,h:3}
]

function readInitialLayout(){
  // Attempt to read server-provided layout JSON from script tag
  const el = document.getElementById('layout-json')
  if(el){
    try{
      const txt = el.textContent.trim()
      if(txt){
        return JSON.parse(txt)
      }
    }catch(e){console.warn('Failed parsing layout-json', e)}
  }
  // Next, try localStorage
  try{
    const raw = localStorage.getItem(DEV_LOCALSTORAGE_KEY)
    if(raw){ return JSON.parse(raw) }
  }catch(e){}
  return DEFAULT_LAYOUT
}

function saveLayoutLocal(layout){
  localStorage.setItem(DEV_LOCALSTORAGE_KEY, JSON.stringify(layout))
}

function renderPanelNode(panel){
  const wrapper = document.createElement('div')
  wrapper.className = 'grid-stack-item'
  wrapper.setAttribute('data-panel-id', panel.id)
  wrapper.setAttribute('tabindex', '0')
  wrapper.setAttribute('role', 'region')
  wrapper.setAttribute('aria-labelledby', `panel-${panel.id}-title`)
  const inner = document.createElement('div')
  inner.className = 'panel'
  inner.innerHTML = `
    <div class="panel-header">
      <div class="panel-title" id="panel-${panel.id}-title">${getPanelTitle(panel.id)}</div>
      <div class="panel-controls">
        <button class="btn secondary btn-move" title="Move" aria-label="Move panel">Move</button>
        <button class="btn secondary btn-settings" title="Settings" aria-label="Panel settings">⚙</button>
        <button class="btn secondary btn-remove" title="Remove" aria-label="Remove panel">✖</button>
      </div>
    </div>
    <div class="panel-body" id="panel-body-${panel.id}">Loading...</div>
  `
  wrapper.appendChild(inner)
  return wrapper
}

function getPanelTitle(id){
  const p = PANEL_REGISTRY.find(x=>x.id===id)
  return p ? p.title : id
}

function renderDashboard(layout){
  const container = document.getElementById('dashboard-grid')
  container.innerHTML = ''
  layout.forEach(p => {
    const node = renderPanelNode(p)
    container.appendChild(node)
    // attempt to load panel data (mocked)
    loadPanelData(p.id).then(html => {
      const body = document.getElementById(`panel-body-${p.id}`)
      if(body) body.innerHTML = html
    })
  })
}

function loadPanelData(panelId){
  // Try fetch to server endpoint; fallback to mocked content
  return new Promise(resolve => {
    fetch(`/api/panels/${panelId}`).then(r=>{
      if(r.ok) return r.json()
      throw new Error('no-api')
    }).then(data=>{
      if(data.html) resolve(data.html)
      else resolve(`<pre>${JSON.stringify(data,null,2)}</pre>`)
    }).catch(()=>{
      // mocked responses
      const mock = {
        stock_alerts: `<ul><li>SKU-1042 — 2 days left</li><li>SKU-2291 — 4 days left</li></ul>`,
        transfers: `<p>2 pending transfers</p>`,
        kpi_strip: `<div style="display:flex;gap:12px"><div class="panel">Total SKUs: 532</div><div class="panel">Alerts: 12</div></div>`,
        recent_activity: `<ol><li>Order SO-1123 created</li><li>Transfer TP-77 ready</li></ol>`
      }
      resolve(mock[panelId] || `<p>No data for ${panelId}</p>`)
    })
  })
}

// Drag & drop via SortableJS (fallback if not available, enable simple swap)
function enableDragDrop(layout){
  const el = document.getElementById('dashboard-grid')
  if(typeof Sortable !== 'undefined'){
    Sortable.create(el, {
      animation:150,
      onEnd: ()=>{
        const newLayout = Array.from(el.children).map((child)=>({id: child.getAttribute('data-panel-id')}))
        saveLayoutLocal(newLayout)
        setSaveState('Saved locally')
      }
    })
  }else{
    // basic click-to-swap: not implemented fully. Keep as no-op.
  }
}

function setSaveState(txt){
  const el = document.getElementById('save-state')
  if(el) el.textContent = txt
}

// Customize modal
function openCustomize(){
  const mb = document.getElementById('modal-backdrop')
  mb.style.display = 'flex'
  const list = document.getElementById('panel-registry')
  list.innerHTML = ''
  PANEL_REGISTRY.forEach(p=>{
    const card = document.createElement('div')
    card.className = 'panel-card'
    card.innerHTML = `<strong>${p.title}</strong><div class="small">${p.description}</div><div style="margin-top:8px"><button class="btn btn-add" data-panel-id="${p.id}">Add</button></div>`
    list.appendChild(card)
  })
}
function closeCustomize(){
  document.getElementById('modal-backdrop').style.display = 'none'
}

function initCustomizeHandlers(){
  document.body.addEventListener('click', (e)=>{
    if(e.target.matches('.btn-add')){
      const id = e.target.getAttribute('data-panel-id')
      const layout = readInitialLayout()
      // avoid duplicates
      if(!layout.find(x=>x.id===id)){
        layout.push({id:id})
        saveLayoutLocal(layout)
        renderDashboard(layout)
      }
    }
    if(e.target.matches('.btn-remove')){
      const panel = e.target.closest('.grid-stack-item')
      const id = panel.getAttribute('data-panel-id')
      let layout = readInitialLayout()
      layout = layout.filter(x=>x.id!==id)
      saveLayoutLocal(layout)
      renderDashboard(layout)
    }
    if(e.target.matches('#open-customize')) openCustomize()
    if(e.target.matches('#close-customize')) closeCustomize()
    if(e.target.matches('#save-layout')){
      const layout = Array.from(document.getElementById('dashboard-grid').children).map(c=>({id:c.getAttribute('data-panel-id')}))
      saveLayoutLocal(layout)
      setSaveState('Saved locally')
      // attempt to save to server
      fetch('/api/dashboard/layouts', {method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({name:'user-layout',layout_json:layout})}).then(r=>{
        if(r.ok) setSaveState('Saved to server')
      }).catch(()=>{})
    }
  })
}

// keyboard accessibility: arrow keys swap panels
function initKeyboardMoves(){
  const grid = document.getElementById('dashboard-grid')
  grid.addEventListener('keydown', (e)=>{
    const target = e.target.closest('.grid-stack-item')
    if(!target) return
    const key = e.key
    if(['ArrowLeft','ArrowRight'].includes(key)){
      e.preventDefault()
      const items = Array.from(grid.children)
      const idx = items.indexOf(target)
      let swapIdx = key==='ArrowLeft' ? idx-1 : idx+1
      if(swapIdx<0 || swapIdx>=items.length) return
      grid.insertBefore(items[swapIdx], items[idx])
      saveLayoutLocal(Array.from(grid.children).map(c=>({id:c.getAttribute('data-panel-id')})))
      setSaveState('Saved locally')
    }
  })
}

function init(){
  const layout = readInitialLayout()
  renderDashboard(layout)
  enableDragDrop(layout)
  initCustomizeHandlers()
  initKeyboardMoves()
  setSaveState('Ready')
}

window.addEventListener('DOMContentLoaded', init)
