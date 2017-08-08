# thunderbolt100k

![screenshot](/screenshot.png)

Build your awesome terminal with [powerlevel9k](https://github.com/bhilburn/powerlevel9k) and this project!

This project is inspired by [JulienLemonde' Configuration](https://github.com/bhilburn/powerlevel9k/wiki/Show-Off-Your-Config#julienlemonde-configuration) for powerlevel9k. The reason I start on this project is that I found it always takes some time to get the weather information each time I press the 'return' button. I want fluent terminal use experience as well as these information displayed and here it is.

**This project is meant to display those information which is not so urgent and may costs some time to fetch from the source.** For example, weather, emails, new comments of given forum and etc.

### Prerequisites

1. Install [Oh My ZSH](http://ohmyz.sh/)
2. Install [powerlevel9k](https://github.com/bhilburn/powerlevel9k) theme
3. Install [nerd-fonts](https://github.com/ryanoasis/nerd-fonts)

### Installation

Before install this project, please make sure you have installed the above prerequisites successfully.

1. Pip install the project:

   ```
   pip install thunderbolt100k
   ```

2. Register an account of [https://www.apixu.com/](https://www.apixu.com/) and copy your api key.

3. Initialize the project (you will be asked for the api key and city location):

   ```bash
   thunderbolt100k init
   ```

4. Open a new shell session and enjoy!

### How it works

As you pip installed, a cmdline tool named `thunderbolt100k` is also installed. Each time you press the 'return' button in the terminal, PL9K will call the `thunderbolt100k` command.

In this command, it will firstly check if the recorded pid is still exist. If the process is not exist, it will then start a new process to poll the corresponding information. So there is a background process to poll necessary information in every given interval and in the foreground (here is the terminal process), it will take much less time to get the information as it is cached already.

### Widgets

**Writting new widget for the project is really simple.** You can write your own widget by creating a `.py` file under `./widgets` folder, just like how the [weather widget](/thunderbolt100k/widgets/weather.py) does.

A widget is a `.py` file under `./widgets` folder which contains at least two functions:

- `fetch`: is used to acquire informations and return the info at the end of the function.
- `display`: is used to show the information in the terminal which is acquired by the `fetch` function. You can print the content in the function or return it and the framework will print it out.

Also, there are some optional functions you can define in the widgets:

- `user_input`: is used to ask for extra user informations and saves them as configurations when `thunderbolt100k init` is executed. For example, an api token.

### Configuration

All the configurations are in the `~/.zshrc`.

By default, all the configurations are set when executing `thunderbolt100k init`. You may only need to edit it when there are some settings change. For example, you can configure the token of https://api.apixu.com, weather location and etc. in `~/.zshrc` file. Here are all the configurations you can set:

```shell
# The token (i.e. api key) for https://api.apixu.com
THUNDERBOLT100K_WEATHER_TOKEN=<ToBeReplaced>
# The city of the weather
THUNDERBOLT100K_WEATHER_CITY=<ToBeReplaced>
# Interval (minutes) to pull the weather info, by default is 5 min
THUNDERBOLT100K_WEATHER_INTERVAL=5
# The final displayed weather info, default is (condition temp last_update)
# Other supported info names:
#     wind 
THUNDERBOLT100K_WEATHER_INFO=(condition temp last_update)
# Customise the colors (default ones as below)
THUNDERBOLT100K_WEATHER_SUN_COLOR="yellow"
THUNDERBOLT100K_WEATHER_RAIN_COLOR="blue"
THUNDERBOLT100K_WEATHER_CLOUD_COLOR="white"
THUNDERBOLT100K_WEATHER_THUNDER_COLOR="yellow"
THUNDERBOLT100K_WEATHER_OVERCAST_COLOR="grey"
THUNDERBOLT100K_WEATHER_SNOW_COLOR="white"
THUNDERBOLT100K_WEATHER_DEFAULT_COLOR="green"
THUNDERBOLT100K_WEATHER_HIGH_TEMP_COLOR="red"
THUNDERBOLT100K_WEATHER_MIDDLE_TEMP_COLOR="yellow"
THUNDERBOLT100K_WEATHER_LOW_TEMP_COLOR="blue"
THUNDERBOLT100K_WEATHER_UPDATE_TIME_COLOR="red"
# Show the update time if it is longer then given time (in minutes)
THUNDERBOLT100K_WEATHER_SHOW_UPDATE_TIME=120
```

### TODO

1. A script to install all the prerequisites?
2. ~~Should we also contains the specific configuration of PL9K? Or, just the widgets?~~
3. ~~Check the main process is running each time the PL9K called the entry function~~
4. Supply a docker container as the cmdline
5. Fix the bug which happens when kill the daemon python process manually