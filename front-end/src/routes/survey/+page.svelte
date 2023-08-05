<script>
    import { onMount } from 'svelte';
    let surveyList = [];
  
    onMount(async () => {
      const response = await fetch('http://192.168.2.18:8000/survey/api/get_survey_list');
      surveyList = await response.json();
    });
  </script>
  
  <main>
    <h1>Survey List</h1>
    <ul>
      {#each surveyList as survey}
        <li>{survey.name}</li>
      {/each}
    </ul>
  </main>
  
  <style>
    /* Your styles go here */
  </style>
  