<script>
	import { isAuthenticated } from './../../../store';
    import {page} from "$app/stores";
    import {onMount} from "svelte";
    import {FetchSurveyData} from "./SurveyData";
    import {Circle2} from 'svelte-loading-spinners';
    import {submitForm} from "./SubmitButton";
    import {goto} from "$app/navigation";

    let Survey_res = {id: 0, title: "", description: "", questions: []};
    let questions = [];

    let responses = [];

    onMount(async () => {
        let survey_id = $page.params["surveyID"];

        try {
            Survey_res = await FetchSurveyData(survey_id);
        } catch (error) {
            console.error(error);
        }

        questions = Survey_res.questions;
    });


    async function getSelectedValues() {
        // @ts-ignore
        let data = [];
        // @ts-ignore
        questions.forEach((ques) => {
            data.push({question_id: ques.id, value: responses[ques.id]});
        })
        let jsonData = {
            "survey_id": Survey_res.id,
            "data": data,
        };
        let submitResult = await submitForm(jsonData);
        if (submitResult) {
            isAuthenticated.set(true);
            goto("/");
        }
    }
</script>

<div class="container">
    {#if (Survey_res.id !== 0)}
        <h1>{Survey_res.title}</h1>
        <p>{Survey_res.description}</p>
        {#each questions as ques}
            <li class="my-3">
                <h2>{ques.text}</h2>
                {#if ques.type === "multi"}

                    <ul class="list-styled">
                        {#each ques.choices as item}
                            <li>
                                <label>
                                    <input type="checkbox" bind:group="{responses[ques.id]}" name="{ques.id}"
                                           value="{item.id}" class="mr-2">
                                    {item.text}
                                </label>
                            </li>
                        {/each}
                    </ul>


                {:else if ques.type === "single"}
                    <ul class="list-styled">
                        {#each ques.choices as item}
                            <li>
                                <label>
                                    <input type="radio" bind:group="{responses[ques.id]}" name="{ques.id}"
                                           value="{item.id}" class="mr-2">
                                    {item.text}
                                </label>
                            </li>
                        {/each}
                    </ul>
                {:else if ques.type === "text"}
                    <input type="text" bind:value={responses[ques.id]} name="{ques.id}" class="form-control">
                {/if}
            </li>
        {/each}

        <input type="submit" class="btn btn-success" placeholder="Submit Form" on:click={getSelectedValues}>
        <!--        <button on:click={getSelectedValues}>Get Selected Values</button>-->

    {:else}
        <div style="position: fixed; left: 50%; top: 50%; transform: translate(-50%, -50%);">
            <Circle2 size="100" color="#FF3E00" unit="px" duration="5s"/>
        </div>

    {/if}
</div>

<style>
    .btn, .btn-success {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
    }

</style>
