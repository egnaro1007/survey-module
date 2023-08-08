export async function submitForm(jsonData) {
    // console.log(formData)
    try {
        // jsonData = {
        //     "survey_id" : "1",
        //     "data" : formData,
        // }
        console.log(jsonData);
        const response = await fetch("http://127.0.0.1:8000/survey/api/survey", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(jsonData),
        });

        if (response.ok) {
            alert("Submitted");
        } else {
            alert("Failed to submit the form!");
        }
    } catch (error) {
        console.error("Error submitting the form:", error);
        alert("An error occurred while submitting the form.");
    }
}