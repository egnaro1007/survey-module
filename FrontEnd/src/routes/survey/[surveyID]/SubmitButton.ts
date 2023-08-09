export async function submitForm(jsonData: { survey_id: any; data: any[] }) : Promise<boolean> {
    try {
        const response = await fetch("http://127.0.0.1:8000/survey/api/survey", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(jsonData),
        });

        if (response.ok) {
            return true;
        } else {
            alert("Please re-submit");
            return false;
        }
    } catch (error) {
        console.error("Error submitting the form:", error);
        alert("An error occurred while submitting the form.");
        return false;
    }
}