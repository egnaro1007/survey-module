<script>
    let username = "";
    let password = "";
    let response_form_server = "";
    async function submitForm() {
        let jsonData;
        try {
            jsonData = {
                "username": username,
                "password": password,
            }
            const response = await fetch("http://127.0.0.1:8000/login/api/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(jsonData),
            });

            if (response.ok) {
                response_form_server = await response.json();

                const accessToken = response_form_server.access_token;
                const accessTokenExpires = Date.now() + response_form_server.access_tolen_expires * 1000;
                localStorage.setItem('access_token', accessToken);
                localStorage.setItem('access_token_expires', accessTokenExpires.toString());

                const refreshToken = response_form_server.refresh_token;
                const refreshTokenExpires = Date.now() + response_form_server.refresh_expires * 1000;
                localStorage.setItem('refresh_token', refreshToken);
                localStorage.setItem('refresh_token_expires', refreshTokenExpires.toString());

            } else {
                alert("Failed to submit the form!");
            }
        } catch (error) {
            console.error("Error submitting the form:", error);
            alert("An error occurred while submitting the form.");
        }
    }
</script>


<section class="vh-100">
    <div class="container py-5 h-100">
        <div class="row d-flex align-items-center justify-content-center h-100">
            <div class="col-md-8 col-lg-7 col-xl-6">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.svg"
                     class="img-fluid" alt="Phone image">
            </div>
            <div class="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
                <form>
                    <!-- Email input -->
                    <div class="form-outline mb-4">
                        <input type="text" id="form1Example13" class="form-control form-control-lg" bind:value = {username}/>
                        <label class="form-label" for="form1Example13">Username</label>
                    </div>

                    <!-- Password input -->
                    <div class="form-outline mb-4">
                        <input type="password" id="form1Example23" class="form-control form-control-lg" bind:value={password} />
                        <label class="form-label" for="form1Example23">Password</label>
                    </div>

                    <div class="d-flex justify-content-around align-items-center mb-4">
                        <!-- Checkbox -->
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="form1Example3" checked />
                            <label class="form-check-label" for="form1Example3"> Remember me </label>
                        </div>
                        <a href="#!">Forgot password?</a>
                    </div>

                    <!-- Submit button -->
                    <button type="submit" class="btn btn-primary btn-lg btn-block"
                    on:click={submitForm}
                    >Sign in</button>

                    <div class="divider d-flex align-items-center my-4">
                        <p class="text-center fw-bold mx-3 mb-0 text-muted">Don't have account ? </p>
                    </div>

                    <button type="submit" class="btn btn-secondary btn-sm  btn-block">Create account</button>

                </form>
            </div>
        </div>
    </div>
</section>

<style>

</style>