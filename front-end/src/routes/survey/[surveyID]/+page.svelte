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

<div class="container">
    {#if Survey_res}
        <h1>{Survey_res.title}</h1>
        <p>{Survey_res.description}</p>
        {#each Survey_res.questions as ques}
            <li class="my-3">
                <h2>{ques.text}</h2>
                {#if ques.type === "multi"}
                    <ul class="list-unstyled">
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
                    <ul class="list-unstyled">
                        {#each ques.choices as item}
                            <li>
                                <label>
                                    <input type="radio" name="{ques.id}" value="{item.id}" class="mr-2">
                                    {item.text}
                                </label>
                            </li>
                        {/each}
                    </ul>
                {:else}
                    <input type="text" name="{ques.id}" class="form-control">
                {/if}
            </li>
        {/each}
    {:else}
        <p>...waiting</p>
    {/if}
    <input type="submit" class="btn btn-success" placeholder="Submit Form" id = "xuanan">

</div>

<style>
    .btn, .btn-success {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
    }

</style>
