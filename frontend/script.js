async function loadInsights() {

    const response = await fetch(
        "https://brewmind-api-xkyw.onrender.com/campaigns/2/insights"
    );

    const data = await response.json();

    document.getElementById("open-rate").innerText =
        `Open Rate: ${data.open_rate}%`;

    document.getElementById("click-rate").innerText =
        `Click Rate: ${data.click_rate}%`;

    document.getElementById("best-city").innerText =
        `Best City: ${data.best_city}`;

    document.getElementById("best-tier").innerText =
        `Best Tier: ${data.best_membership_tier}`;
}

async function loadPerformance() {

    const response = await fetch(
        "https://brewmind-api-xkyw.onrender.com/campaigns/2/performance"
    );

    const data = await response.json();

    document.getElementById("recipients").innerText =
        `Recipients: ${data.total_recipients}`;

    document.getElementById("sent").innerText =
        `Sent: ${data.sent}`;

    document.getElementById("opened").innerText =
        `Opened: ${data.opened}`;

    document.getElementById("clicked").innerText =
        `Clicked: ${data.clicked}`;
}

loadInsights();
loadPerformance();