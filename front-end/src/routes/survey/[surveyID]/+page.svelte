<script>
    import { page } from "$app/stores";
    import { onMount } from "svelte";
    import {writable} from "svelte/store";

    let survey_res = writable(null);

    onMount(async () => {
        const survey_id = $page.params.surveyID;
        const response = await fetch('http://192.168.2.18:8000/survey/api/survey?survey_id='+survey_id);
        survey_res = await response.json();
    });
</script>

<main>
    <h1>{survey_res.title}</h1>
    <p>{survey_res.description}</p>
    <ul>
        {#each survey_res.questions as ques}
            <p>hello</p>
        {/each}
    </ul>
</main>
