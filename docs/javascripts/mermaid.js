mermaid.initialize({ startOnLoad: false, securityLevel: "loose" });

window.addEventListener("DOMContentLoaded", () => {
  mermaid.run({ querySelector: ".mermaid" });
});
