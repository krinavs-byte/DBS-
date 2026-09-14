document.addEventListener('DOMContentLoaded', function () {
  const chart = document.getElementById('landing-chart');
  if (chart) {
    chart.innerHTML = miniLineChart([30, 45, 38, 60, 52, 70, 65, 80], '#6F4A6F');
  }
});

function miniLineChart(vals, color) {
  const w = 560;
  const h = 150;
  const max = Math.max(...vals);
  const min = Math.min(...vals);
  const pts = vals.map((v, i) => {
    const x = (i / (vals.length - 1)) * w;
    const y = h - ((v - min) / (max - min || 1)) * (h - 20) - 10;
    return x + ',' + y;
  }).join(' ');
  const area = `0,${h} ${pts} ${w},${h}`;
  return `<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="none">
    <polygon points="${area}" fill="${color}" opacity="0.12"></polygon>
    <polyline points="${pts}" fill="none" stroke="${color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></polyline>
  </svg>`;
}
