export async function submitForm(formData) {
    let testJson;
    try {
        testJson = {
            "survey_id" : "1",
            "data" :[

            ]
        }
        const response = await fetch("http://192.168.2.18:8000/survey/api/survey", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(testJson),
        });

        if (response.ok) {
            alert("Form submitted successfully!");
        } else {
            alert("Failed to submit the form!");
        }
    } catch (error) {
        console.error("Error submitting the form:", error);
        alert("An error occurred while submitting the form.");
    }
}