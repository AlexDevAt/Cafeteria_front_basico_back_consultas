function $(id){ return document.getElementById(id); }

function clearResults(){
  $("resultTitle").textContent = "Resultados";
  $("resultMeta").textContent = "Presiona un botón para consultar.";
  $("resultBody").innerHTML = '<div class="empty">Sin resultados todavía.</div>';

  $("statusText").textContent = "Listo.";
  $("statusText").className = "muted";
  const pill = $("statusPill");
  pill.textContent = "—";
  pill.className = "pill";
}

function setStatus(text, kind){
  $("statusText").textContent = text;
  $("statusText").className = kind === "bad" ? "bad" : (kind === "ok" ? "ok" : "muted");

  const pill = $("statusPill");
  pill.textContent = kind === "ok" ? "OK" : (kind === "bad" ? "ERROR" : "…");
  pill.className = "pill " + (kind || "");
}

function humanKey(key){
  return String(key).replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase());
}

function escapeHtml(s){
  return String(s)
    .replaceAll("&","&amp;")
    .replaceAll("<","&lt;")
    .replaceAll(">","&gt;")
    .replaceAll('"',"&quot;")
    .replaceAll("'","&#039;");
}

function renderObjectAsCards(obj){
  const keys = Object.keys(obj);
  if (keys.length === 0) return '<div class="empty">Objeto vacío.</div>';

  let html = `<div class="cards">`;
  html += `<div class="card"><div class="cardTitle">Resumen</div><div class="kv">`;
  for (const k of keys){
    html += `<div class="k">${escapeHtml(humanKey(k))}</div><div class="v">${escapeHtml(obj[k])}</div>`;
  }
  html += `</div></div></div>`;
  return html;
}

function renderArrayAsTable(arr){
  if (arr.length === 0) return '<div class="empty">No hay resultados.</div>';

  // columnas = unión de keys (por si una fila trae algo extra)
  const colSet = new Set();
  arr.forEach(row => {
    if (row && typeof row === "object"){
      Object.keys(row).forEach(k => colSet.add(k));
    }
  });
  const cols = Array.from(colSet);

  let html = `<table><thead><tr>`;
  cols.forEach(c => html += `<th>${escapeHtml(humanKey(c))}</th>`);
  html += `</tr></thead><tbody>`;

  arr.forEach(row => {
    html += `<tr>`;
    cols.forEach(c => {
      const val = row && typeof row === "object" && c in row ? row[c] : "";
      html += `<td>${escapeHtml(val)}</td>`;
    });
    html += `</tr>`;
  });

  html += `</tbody></table>`;
  return html;
}

function renderPretty(data){
  // FastAPI error típico: {"detail":"..."}
  if (data && typeof data === "object" && !Array.isArray(data) && ("detail" in data) && Object.keys(data).length === 1){
    return `<div class="card"><div class="cardTitle">Detalle del error</div><div class="kv">
      <div class="k">Mensaje</div><div class="v">${escapeHtml(data.detail)}</div>
    </div></div>`;
  }

  if (Array.isArray(data)) return renderArrayAsTable(data);
  if (data && typeof data === "object") return renderObjectAsCards(data);

  return `<div class="card"><div class="cardTitle">Respuesta</div><div>${escapeHtml(data)}</div></div>`;
}

async function callApi(title, path){
  const base = $("baseUrl").value.trim().replace(/\/$/, "");
  const url = base + path;

  $("resultTitle").textContent = title;
  $("resultMeta").textContent = `GET ${url}`;
  $("resultBody").innerHTML = `<div class="empty">Cargando...</div>`;
  setStatus("Cargando…", "");

  try{
    const resp = await fetch(url);
    const ct = resp.headers.get("content-type") || "";

    let data;
    if (ct.includes("application/json")) data = await resp.json();
    else data = await resp.text();

    if (!resp.ok){
      setStatus(`Error ${resp.status}`, "bad");
      $("resultBody").innerHTML = renderPretty(data);
      return;
    }

    setStatus("Consulta realizada correctamente ", "ok");
    $("resultBody").innerHTML = renderPretty(data);

  } catch (err){
    setStatus("Error de conexión ", "bad");
    $("resultBody").innerHTML = renderPretty({ detail: String(err) });
  }
}

// estado inicial
clearResults();