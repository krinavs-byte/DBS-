// Minimal client script: renders panels and allows saving a new layout
document.addEventListener("DOMContentLoaded", function () {
  const panelsDiv = document.getElementById("panels");
  let layout = window.INITIAL_LAYOUT || { panels: [] };

  function render() {
    panelsDiv.innerHTML = "";
    layout.panels.forEach((p, i) => {
      const el = document.createElement("div");
      el.className = "panel";
      el.dataset.panelId = p.id;
      el.innerHTML = `<h3>${p.id}</h3><pre>${JSON.stringify(p.position)}</pre>
        <button data-move-up="${i}">↑</button>
        <button data-move-down="${i}">↓</button>`;
      panelsDiv.appendChild(el);
    });
  }

  function move(index, dir) {
    const newIndex = index + dir;
    if (newIndex < 0 || newIndex >= layout.panels.length) return;
    const [item] = layout.panels.splice(index, 1);
    layout.panels.splice(newIndex, 0, item);
    render();
  }

  panelsDiv.addEventListener("click", (e) => {
    const up = e.target.getAttribute("data-move-up");
    const down = e.target.getAttribute("data-move-down");
    if (up !== null) move(parseInt(up, 10), -1);
    if (down !== null) move(parseInt(down, 10), 1);
  });

  document.getElementById("customize").addEventListener("click", async () => {
    // save as user's layout (GET current to know if there is an id)
    const resp = await fetch("/api/dashboard/layouts/current");
    let data = await resp.json();
    let payload = { layout_json: layout };
    if (resp.status === 200 && data.id) {
      // update existing layout (we need current version)
      payload.version = data.version;
      const putResp = await fetch(`/api/dashboard/layouts/${data.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      if (putResp.status === 200) {
        alert("Layout saved");
      } else if (putResp.status === 409) {
        const body = await putResp.json();
        alert("Save failed: stale layout. Reloading current layout.");
        // reload current layout from server
        const r2 = await fetch("/api/dashboard/layouts/current");
        const updated = await r2.json();
        layout = updated.layout_json;
        render();
      } else {
        const b = await putResp.json();
        alert("Save failed: " + JSON.stringify(b));
      }
    } else {
      // create new layout
      const postResp = await fetch("/api/dashboard/layouts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      if (postResp.status === 201) {
        alert("Layout created");
      } else {
        const b = await postResp.json();
        alert("Create failed: " + JSON.stringify(b));
      }
    }
  });

  render();
});
