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
