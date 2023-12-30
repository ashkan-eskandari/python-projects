 const weather_wrapper = document.getElementById("weather_wrapper")
    const weather_spinner = document.getElementById("weather_spinner")
    const weather_condition = document.getElementById("weatherCondition")
    const weather_temperature = document.getElementById("temperature")
    const weather_location = document.getElementById("weather_location")
    const weather_icon = document.getElementById("weather_icon")
    const get_weather_button = document.getElementById("get_weather_button")
    get_weather_button.addEventListener("click", async function () {
        weather_wrapper.classList.add("d-none")
        weather_spinner.classList.remove("d-none")
        await fetch("/weather", {
            method: "post",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({}),
        }).then(response => response.json()).then(data => {

            console.log(data)
            let temperature = data.temperature
            let condition = data.condition
            let city = data.city
            let icon_png = `https://openweathermap.org/img/wn/${data.icon}@2x.png`

            weather_spinner.classList.add("d-none")
            weather_wrapper.classList.remove("d-none")
            weather_condition.innerText = condition
            weather_location.innerText = city
            weather_temperature.innerText = temperature
            weather_icon.src = icon_png
        }).catch(error => {
            console.error('Error:', error);
        });

    })

