export async function FetchSurveyData(survey_id) {
    const response = await fetch(
        "http://192.168.2.18:8000/survey/api/survey?survey_id=" + survey_id
    );
    if (response.ok) {
        return response.json();
    } else {
        throw new Error("Failed to fetch survey data.");
    }
}
