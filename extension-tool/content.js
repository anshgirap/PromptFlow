// ====== Track selected text ======
let lastSelection = "";

document.addEventListener("selectionchange", () => {
  const sel = window.getSelection();
  if (sel && sel.toString().trim()) {
    lastSelection = sel.toString();
  }
});

// ====== Floating Bubble ======
const bubble = document.createElement("div");
const img = document.createElement("img");
img.src = chrome.runtime.getURL("/assets/logosmall.png");
img.style.width = "50%";
img.style.height = "50%";
img.style.objectFit = "contain";
bubble.appendChild(img);

Object.assign(bubble.style, {
  position: "fixed",
  bottom: "22px",
  right: "22px",
  width: "52px",
  height: "52px",
  background: "linear-gradient(135deg, #b11212, #5a0505)",
  borderRadius: "50%",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  cursor: "pointer",
  zIndex: "999999",
  boxShadow: "0 0 18px rgba(133, 3, 3, 0.9)",
  transition: "transform 0.2s ease, box-shadow 0.2s ease"
});

bubble.onmouseenter = () => {
  bubble.style.transform = "scale(1.12)";
  bubble.style.boxShadow = "0 0 30px rgba(255,60,60,0.9)";
};

bubble.onmouseleave = () => {
  bubble.style.transform = "scale(1)";
  bubble.style.boxShadow = "0 0 18px rgba(255,60,60,0.7)";
};

document.body.appendChild(bubble);

// ====== Panel ======
const panel = document.createElement("div");
panel.innerHTML = `
  <div style="font-weight:700;margin-bottom:10px;font-size:16px">PromptFlow</div>

  <textarea id="pf_input" style="
    width: calc(100% - 30px);
    height:140px;
    background: rgba(255,255,255,0.03);
    color:white;
    border:none;
    border-radius:12px;
    padding:14px;
    font-size:13.5px;
    line-height:1.45;
    resize:none;
    outline:none;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.04);
  "></textarea>

  <button id="pf_btn" style="
    margin-top:12px;
    width:100%;
    padding:12px;
    background: linear-gradient(135deg, #c41414, #6a0505);
    border:none;
    border-radius:12px;
    color:white;
    font-weight:700;
    cursor:pointer;
    letter-spacing:0.3px;
    box-shadow: 0 10px 28px rgba(200,20,20,0.35);
  ">Optimize</button>

  <div id="pf_spinner" style="
    position:absolute;
    top:14px;
    right:16px;
    width:14px;
    height:14px;
    border-radius:50%;
    border:2px solid rgba(255,255,255,0.15);
    border-top:2px solid #ff3b3b;
    display:none;
  "></div>

  <div id="pf_out" style="margin-top:12px;font-size:12px;white-space:pre-wrap"></div>

  <div id="pf_copy" style="
    margin-top:10px;
    font-size:11px;
    color:#ff4d4d;
    cursor:pointer;
    text-align:left;
    display:none;
    user-select:none;
  ">Copy</div>
`;

Object.assign(panel.style, {
  position: "fixed",
  bottom: "90px",
  right: "20px",
  width: "340px",
  background: "rgba(18,18,18,0.72)",
  backdropFilter: "blur(22px) saturate(180%)",
  WebkitBackdropFilter: "blur(22px) saturate(180%)",
  borderRadius: "16px",
  padding: "16px",
  color: "white",
  display: "none",
  zIndex: "999999",
  boxShadow: "0 40px 80px rgba(0,0,0,0.65), inset 0 0 0 1px rgba(255,255,255,0.06)",
  opacity: "0",
  transform: "translateY(14px) scale(0.96)",
  transition: "opacity 0.28s cubic-bezier(.2,.9,.2,1), transform 0.32s cubic-bezier(.2,.9,.2,1)"
});

document.body.appendChild(panel);

// ====== Toggle Panel ======
bubble.onclick = () => {
  if (panel.style.display === "none") {
    panel.style.display = "block";
    requestAnimationFrame(() => {
      panel.style.opacity = "1";
      panel.style.transform = "translateY(0) scale(1)";
    });
  } else {
    panel.style.opacity = "0";
    panel.style.transform = "translateY(10px) scale(0.98)";
    setTimeout(() => {
      panel.style.display = "none";
    }, 250);
  }

  panel.querySelector("#pf_input").value = lastSelection;
};

// ====== Button ======
panel.querySelector("#pf_btn").onclick = async () => {
  const text = panel.querySelector("#pf_input").value.trim();
  const out = panel.querySelector("#pf_out");
  const spinner = panel.querySelector("#pf_spinner");
  const copy = panel.querySelector("#pf_copy");

  if (!text) {
    out.innerText = "Enter some text first.";
    return;
  }

  spinner.style.display = "block";
  spinner.style.animation = "pfspin 0.8s linear infinite";
  copy.style.display = "none";

  try {
    const res = await fetch("https://promptflow-backend-75nt.onrender.com/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        prompt: text,
        platform: "PromptFlow Extension"
      })
    });

    const data = await res.json();
    spinner.style.display = "none";

    if (data.error) {
      out.innerText = "Error: " + data.error;
      return;
    }

    out.innerText = data.expanded_prompt;
    copy.style.display = "block";
    copy.innerText = "Copy";

    copy.onclick = () => {
      navigator.clipboard.writeText(data.expanded_prompt);
      copy.innerText = "Copied";
      setTimeout(() => (copy.innerText = "Copy"), 1200);
    };

  } catch (e) {
    spinner.style.display = "none";
    out.innerText = "Network error.";
  }
};

// ====== Spinner Animation ======
const style = document.createElement("style");
style.innerHTML = `
@keyframes pfspin {
  to { transform: rotate(360deg); }
}
`;
document.head.appendChild(style);