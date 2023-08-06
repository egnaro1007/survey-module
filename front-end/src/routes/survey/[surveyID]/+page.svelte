<script>
    import {page} from "$app/stores";
    import {onMount} from "svelte";
    import {FetchSurveyData} from "./SurveyData.js";
    import { Circle2 } from 'svelte-loading-spinners';
    import {submitForm} from "./SubmitButton.js";
    import { afterUpdate, onDestroy } from 'svelte';


    let Survey_res;
    let textInput = "";

    onMount(async () => {
        const survey_id = $page.params.surveyID;

        try {
            Survey_res = await FetchSurveyData(survey_id);
        } catch (error) {
            console.error(error);
        }
    });

    let checkboxes = [];
    let data = {};

    afterUpdate(() => {
        checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach((checkbox) => {
            checkbox.addEventListener('change', () => {
                if(checkbox.checked) {
                    if(!data[checkbox.name]) {
                        data[checkbox.name] = [];
                    }
                    data[checkbox.name].push(checkbox.value);
                }
                else{
                    data[checkbox.name].splice(data[checkbox.name].indexOf(checkbox.value), 1);
                }
            });
        });
        let radios = document.querySelectorAll('input[type="radio"]');
        radios.forEach((radio) => {
            radio.addEventListener('change', () => {
                if(radio.checked) {
                    data[radio.name] = radio.value;
                }
            });
        });
        console.log(data);
    });


</script>

<div class="container">
    {#if Survey_res}
        <h1>{Survey_res.title}</h1>
        <p>{Survey_res.description}</p>
        {#each Survey_res.questions as ques}
            <li class="my-3">
                <h2>{ques.text}</h2>
                {#if ques.type === "multi"}

                    <ul class="list-styled">
                        {#each ques.choices as item}
                            <li>
                                <label>
                                    <input type="checkbox" name="{ques.id}" value="{item.id}" class="mr-2">
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
                                    <input type="radio" name="{ques.id}" value="{item.id}" class="mr-2" >
                                    {item.text}
                                </label>
                            </li>
                        {/each}
                    </ul>
                {:else}
                    <input type="text" name="{ques.id}" class="form-control" bind:value={textInput} >
                {/if}
            </li>
        {/each}

        <input type="submit" class="btn btn-success" placeholder="Submit Form" on:click={submitForm(textInput)}>

    {:else}
        <div style="position: fixed; left: 50%; top: 50%; transform: translate(-50%, -50%);">
            <Circle2 size="100" color="#FF3E00" unit="px" duration="5s" />
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
