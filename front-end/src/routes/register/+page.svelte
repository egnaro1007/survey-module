<div class="container mt-2 mb-4">
    <div class="row justify-content-md-center">
        <div class="col-sm-4 border border-primary shadow rounded pt-2">
            <div class="text-center"><img src="https://placehold.it/80x80" class="rounded-circle border p-1"></div>
            <div class="col-sm-12">
                <form method="post" id="singnupFrom" onSubmit="return validation();">
                    <div class="form-group">
                        <label class="font-weight-bold">Email</label>
                        <div class="input-group">
                            <input type="email" name="email" id="email" class="form-control" placeholder="Enter valid email">
                            <div class="input-group-append"><button type="button" class="btn btn-primary" onClick="return emailCheck();"><i class="fa fa-envelope"></i></button></div>
                        </div>
                    </div>
                    <div id="next-form" class="collapse">
                        <div class="form-group">
                            <label class="font-weight-bold">User Name <small class="text-danger"><em>This will be your login name!</em></small></label>
                            <input type="text" name="username" id="username" class="form-control" placeholder="Choose your user name">
                        </div>
                        <div class="form-group">
                            <label class="font-weight-bold">Phone #</label>
                            <input type="text" name="phone" id="phone" class="form-control" placeholder="(000)-(0000000)">
                        </div>
                        <div class="form-group">
                            <label class="font-weight-bold">Password</label>
                            <input type="password" name="password" id="password" class="form-control" placeholder="***********">
                        </div>
                        <div class="form-group">
                            <label class="font-weight-bold">Confirm Password</label>
                            <input type="password" name="cpassword" id="cpassword" class="form-control" placeholder="***********">
                            <em id="cp"></em>
                        </div>
                        <div class="form-group">
                            <label><input type="checkbox" name="condition" id="condition"> I agree with the <a href="javascript:;">Terms & Conditions</a> for Registration.</label>
                        </div>
                        <div class="form-group">
                            <input type="submit" name="submit" value="Sign Up" class="btn btn-block btn-danger">
                        </div>
                    </div> <!--/.next-form-->
                </form>
            </div>
        </div>
    </div>
</div>




<!--<section class="vh-100">-->
<!--    <div class="container py-5 h-100">-->
<!--        <div class="row d-flex align-items-center justify-content-center h-100">-->
<!--            <div class="col-md-8 col-lg-7 col-xl-6">-->
<!--                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.svg"-->
<!--                     class="img-fluid" alt="Phone image">-->
<!--            </div>-->
<!--            <div class="col-md-7 col-lg-5 col-xl-5 offset-xl-1">-->
<!--                <form>-->
<!--                    &lt;!&ndash; First name input &ndash;&gt;-->
<!--                    <div class="form-outline mb-4">-->
<!--                        <input type="text" id = firstName class="form-control form-control-lg"/>-->
<!--                        <label class="form-label" for="firstName">First Name</label>-->
<!--                    </div>-->

<!--                    &lt;!&ndash; Last name input &ndash;&gt;-->
<!--                    <div class="form-outline mb-4">-->
<!--                        <input type="text" id = lastName class="form-control form-control-lg"/>-->
<!--                        <label class="form-label" for="lastName">First Name</label>-->
<!--                    </div>-->

<!--                    &lt;!&ndash; Username input &ndash;&gt;-->
<!--                    <div class="form-outline mb-4">-->
<!--                        <input type="text" id = username class="form-control form-control-lg"/>-->
<!--                        <label class="form-label" for="username">Username</label>-->
<!--                    </div>-->

<!--                    &lt;!&ndash; Email input &ndash;&gt;-->
<!--                    <div class="form-outline mb-4">-->
<!--                        <input type="text" id="form1Example13" class="form-control form-control-lg"/>-->
<!--                        <label class="form-label" for="form1Example13">Email</label>-->
<!--                    </div>-->

<!--                    &lt;!&ndash; Password input &ndash;&gt;-->
<!--                    <div class="form-outline mb-4">-->
<!--                        <input type="password" id="form1Example23" class="form-control form-control-lg"/>-->
<!--                        <label class="form-label" for="form1Example23">Password</label>-->
<!--                    </div>-->



<!--                    <div class="d-flex justify-content-around align-items-center mb-4">-->
<!--                        &lt;!&ndash; Checkbox &ndash;&gt;-->
<!--                        <div class="form-check">-->
<!--                            <input class="form-check-input" type="checkbox" value="" id="form1Example3" checked />-->
<!--                            <label class="form-check-label" for="form1Example3"> Remember me </label>-->
<!--                        </div>-->
<!--                        <a href="#!">Forgot password?</a>-->
<!--                    </div>-->

<!--                    &lt;!&ndash; Submit button &ndash;&gt;-->
<!--                    <button type="submit" class="btn btn-primary btn-lg btn-block"-->
<!--                            on:click={submitForm}-->
<!--                    >Sign in</button>-->

<!--                    <div class="divider d-flex align-items-center my-4">-->
<!--                        <p class="text-center fw-bold mx-3 mb-0 text-muted">Don't have account ? </p>-->
<!--                    </div>-->

<!--                    <button type="submit" class="btn btn-secondary btn-sm  btn-block">Create account</button>-->

<!--                </form>-->
<!--            </div>-->
<!--        </div>-->
<!--    </div>-->
<!--</section>-->