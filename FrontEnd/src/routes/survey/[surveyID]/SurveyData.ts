export async function FetchSurveyData(survey_id : String) : Promise<String>{
    const response = await fetch(
        "http://127.0.0.1:8000/survey/api/survey?survey_id=" + survey_id
    );
    if (response.ok) {
        return response.json();
    } else {
        throw new Error("Failed to fetch survey data.");
    }
}
