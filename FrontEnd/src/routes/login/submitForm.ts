export async function submitForm(username: string, password: string): Promise<boolean> {
    let jsonData;
    let response_form_server = {
        "access_token": "",
        "access_token_expires": 0,
        "refresh_token": "",
        "refresh_expires": 0,
    };
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
            const accessTokenExpires = Date.now() + response_form_server.access_token_expires * 1000;
            localStorage.setItem('access_token', accessToken);
            localStorage.setItem('access_token_expires', accessTokenExpires.toString());

            const refreshToken = response_form_server.refresh_token;
            const refreshTokenExpires = Date.now() + response_form_server.refresh_expires * 1000;
            localStorage.setItem('refresh_token', refreshToken);
            localStorage.setItem('refresh_token_expires', refreshTokenExpires.toString());
            return true;

        } else {
            return false;
        }
    } catch (error) {
        return false;
    }
}