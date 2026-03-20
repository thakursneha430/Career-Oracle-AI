// 🎯 Select form and result area
const form = document.getElementById("career-form");
const resultDiv = document.getElementById("result");

// 🚀 Handle form submit
form.addEventListener("submit", async function (e) {
    e.preventDefault(); // stop page reload

    // 📥 Get user input
    const interests = document.getElementById("interests").value;
    const skills = document.getElementById("skills").value;
    const personality = document.getElementById("personality").value;

    // 🔄 Show loading
    resultDiv.innerHTML = "🔮 Predicting your future...";

    try {
        // 🌐 Send request to Flask API
        const response = await fetch("/api/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                interests: interests,
                skills: skills,
                personality: personality
            })
        });

        const data = await response.json();

        // 🎉 Show result
        resultDiv.innerHTML = `
            <h2>🔮 Your Future Career: ${data.career}</h2>
            <p>${data.reason}</p>
            <p>📊 Confidence: ${data.confidence}%</p>
        `;

    } catch (error) {
        // ❌ Error handling
        resultDiv.innerHTML = "⚠️ Something went wrong. Try again!";
        console.error(error);
    }
});