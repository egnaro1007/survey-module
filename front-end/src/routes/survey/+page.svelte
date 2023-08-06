<script>
  import { onMount } from 'svelte';
  let surveyList = [];

  onMount(async () => {
    const response = await fetch('http://127.0.0.1:8000/survey/api/get_survey_list');
    surveyList = await response.json();
  });
</script>

<main>
  <h1>Survey List</h1>
  <ul class="survey-list">
    {#each surveyList as survey}
      <li class="survey-item">
        <h2>{survey.title}</h2>
        <p>{survey.description}</p>
        <a href='survey/{survey.id}' target="_self" class="join-button">Join Survey</a>
      </li>
    {/each}
  </ul>
</main>

<style>
  /* Your styles go here */

  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
  }

  .survey-list {
    list-style: none;
    padding: 0;
  }

  .survey-item {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: #f9f9f9;
  }

  h1 {
    color: limegreen;
  }

  h2 {
    margin: 0;
    color: #333;
  }

  p {
    margin: 0;
    color: #555;
  }

  .join-button {
    display: inline-block;
    padding: 10px 20px;
    background-color: limegreen;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s;
    align-content: center;
    align-self: center;

  }

  .join-button:hover {
    background-color: white;
    color: limegreen;
  }
</style>
