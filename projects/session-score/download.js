// The release build produces this filename only after Apple's ticket passes validation.
const project = "OmTheLast/Session-Score";
const assetName = "Session-Score-macOS-arm64-notarized.zip";
async function showMacDownload() {
  const response = await fetch("https://api.github.com/repos/" + project + "/releases/latest",
    {credentials: "omit", referrerPolicy: "no-referrer"});
  if (!response.ok) return;
  const release = await response.json();
  const asset = release.assets.find(item => item.name === assetName && item.state === "uploaded" && item.size > 0);
  if (!asset) return;
  const link = document.getElementById("install");
  link.href = "https://github.com/" + project + "/releases/download/" + encodeURIComponent(release.tag_name) + "/" + assetName;
  link.textContent = "Download for Mac";
  document.getElementById("availability").textContent =
    release.tag_name + " · Apple silicon · Unzip and move Session Score to Applications.";
}
showMacDownload().catch(() => { /* The source and releases links also work offline from the API. */ });
