<script lang="ts">
  import { goto } from "$app/navigation";
  import { submitForm } from "./submitForm";
  import { isAuthenticated } from "../../store";

  let username: string = "";
  let password: string = "";

  function createAccount() {
    goto("/register");
  }

  let submitLogin = async () => {
    let result = await submitForm(username, password);
    if (result) {
      goto("/survey");
      isAuthenticated.set(true);
    } else {
      alert("Wrong username or password");
    }
  };
  
</script>

<section class="vh-100">
  <div class="container py-5 h-100">
    <div class="row d-flex align-items-center justify-content-center h-100">
      <div class="col-md-8 col-lg-7 col-xl-6">
        <img
          src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.svg"
          class="img-fluid"
          alt="Phone image"
        />
      </div>
      <div class="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
        <form>
          <!-- Email input -->
          <div class="form-outline mb-4">
            <input
              type="text"
              id="form1Example13"
              class="form-control form-control-lg"
              bind:value={username}
            />
            <label class="form-label" for="form1Example13">Username</label>
          </div>

          <!-- Password input -->
          <div class="form-outline mb-4">
            <input
              type="password"
              id="form1Example23"
              class="form-control form-control-lg"
              bind:value={password}
            />
            <label class="form-label" for="form1Example23">Password</label>
          </div>

          <div class="d-flex justify-content-around align-items-center mb-4">
            <!-- Checkbox -->
            <div class="form-check">
              <input
                class="form-check-input"
                type="checkbox"
                value=""
                id="form1Example3"
                checked
              />
              <label class="form-check-label" for="form1Example3">
                Remember me
              </label>
            </div>
            <a href="#!">Forgot password?</a>
          </div>

          <!-- Submit button -->
          <button
            type="submit"
            class="btn btn-primary btn-lg btn-block"
            on:click={submitLogin}
            >Sign in
          </button>

          <div class="divider d-flex align-items-center my-4">
            <p class="text-center fw-bold mx-3 mb-0 text-muted">
              Don't have account ?
            </p>
          </div>
        </form>
        <button
          type="submit"
          class="btn btn-secondary btn-sm btn-block"
          on:click={createAccount}
          >Create account
        </button>
      </div>
    </div>
  </div>
</section>

<style>
</style>
