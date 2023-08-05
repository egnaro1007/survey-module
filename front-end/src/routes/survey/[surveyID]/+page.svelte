<script>
    import {page} from "$app/stores";
    import {onMount} from "svelte";

    let Survey_res;

    onMount(async () => {
        const survey_id = $page.params.surveyID;
        const response = await fetch(
            "http://192.168.2.18:8000/survey/api/survey?survey_id=" + survey_id
        );
        if (response.ok) {
            Survey_res = await response.json();
        }
    });
</script>

{#if Survey_res}
    <h1>{Survey_res.title}</h1>
    <p>{Survey_res.description}</p>

    <ul>
        {#each Survey_res.questions as ques}
            <h2>{ques.text}</h2>
            {#if ques.type === "multi"}
                <ul>
                    {#each ques.choices as item}
                        <li>
                            <label>
                                <input type="checkbox" name="{ques.id}" value="{item.id}">
                                {item.text}
                            </label>
                        </li>
                    {/each}
                </ul>
            {:else if ques.type === "single"}
                <ul>
                    {#each ques.choices as item}
                        <li>
                            <label>
                                <input type="radio" name="{ques.id}" value="{item.id}">
                                {item.text}
                            </label>
                        </li>
                    {/each}
                </ul>
            {:else}
                <input type="text" name="{ques.id}">
            {/if}
        {/each}
    </ul>
{:else}
    <p>...waiting</p>
{/if}
<style>
    /* Custom styles for the survey page */

    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 20px;
        padding: 0;
        background-color: #f7f7f7;
    }

    h1 {
        color: #007bff; /* Change header color to a nice blue */
        font-size: 32px; /* Increase the font size for the header */
        margin-bottom: 20px; /* Add more spacing below the header */
        text-align: center; /* Center align the header */
    }


    p {
        color: #555;
        font-size: 16px;
        margin-bottom: 20px;
    }

    /* Add a border around the survey box */
    ul {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 15px;
    }


    li {
        margin-bottom: 5px;
    }

    /* Style for radio buttons */
    input[type="radio"] {
        transform: scale(1.2); /* Slightly increase the size of the radio button */
    }

    /* Style for checkboxes */
    input[type="checkbox"] {
        transform: scale(1.2); /* Slightly increase the size of the checkbox */
    }


    label {
        cursor: pointer;
    }

    label:hover {
        color: #555;
        background-color: #e9e9e9;
        border-radius: 5px;
    }

    label:hover {
        color: #007bff;
    }


    h2 {
        background-color: #f0f0f0; /* Add a light background color to the question */
        padding: 10px; /* Add padding around the question */
        border-radius: 5px; /* Round the corners of the question box */
    }
    /* Center align the survey box */
    ul {
        max-width: 600px; /* Set a maximum width to the survey box */
        margin: 0 auto; /* Center align the survey box horizontally */
    }

</style>