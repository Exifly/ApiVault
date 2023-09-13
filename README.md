<h1 align="center">
    <img src="https://raw.githubusercontent.com/Exifly/ApiVault/main/frontend/public/img/apivault-full-dark-nobg.png#gh-dark-mode-only" alt="apivault dark" width="200">
    <img src="https://raw.githubusercontent.com/Exifly/ApiVault/main/frontend/public/img/apivault-full-light-nobg.png#gh-light-mode-only" alt="ApiVault" width="200">
  <br>
</h1>

![screenshot](./assets/Hero.png)

<p align="center">
<a href="https://www.producthunt.com/posts/apivault?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-apivault" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=414441&theme=light" alt="Apivault - Your&#0032;gateway&#0032;to&#0032;a&#0032;world&#0032;of&#0032;public&#0032;APIs&#0046; | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>
</p>

<p align="center">
    <a href="https://github.com/Exifly/ApiVault/tree/release" alt="Stable">
        <img src="https://img.shields.io/badge/stable-2.1.0-blue?style=for-the-badge" /></a>
    <a href="https://github.com/exifly/apivault/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/exifly/apivault?style=for-the-badge" /></a>
    <a href="https://github.com/exifly/apivault/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/exifly/apivault?style=for-the-badge" /></a>
    <a href="https://github.com/exifly/apivault/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/actions/workflow/status/exifly/apivault/node.js.yml?style=for-the-badge" /></a>
    <a href="https://discord.gg/e4KbstNqtk" alt="Discord Server">
        <img src="https://dcbadge.vercel.app/api/server/e4KbstNqtk" /></a>
<br>    
</p>

<p align="center">
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
</p>

<h1 align="center">
  <a href="https://github.com/Exifly/ApiVault/issues/new?assignees=&labels=add+api&template=add-your-api.md&title=%5BAPIFT%5D">Click here to submit your API</a>
</h1>

<div align="center">

  # Built with
  [![Nuxt.js](https://img.shields.io/badge/nuxt.js-35495E?style=for-the-badge&logo=nuxtdotjs&logoColor=4FC08D)](https://nuxt.com/)
  [![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)](https://vuejs.org/)
  [![Django](https://img.shields.io/badge/Django-000000?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/start/overview/)




</div>

<hr />

# Prerequisites
Before starting to use the software make sure you have <a href="https://www.docker.com/">docker</a> installed.

# How To Use

## Clone the repository
```bash
git clone https://github.com/exifly/ApiVault
```

## Set .env file
Inside root repository folder rename .env.dev file
```bash
cat .env.dev > .env
```

Inside /frontend folder rename .env.sample file
```bash
cd frontend
cat .env.dev > .env
```

Same action inside /backend folder
```bash
cd backend
cat .env.dev > .env
```

## Client/Server side using Docker
```bash
# Go into the root folder
cd ApiVault

# Run docker
docker-compose up
```

## Important note:
On first docker-compose launch, your terminal could tell you:
```bash
database_dev  | 2023-05-26 13:38:01.598 UTC [83] ERROR:  relation "vault_api" does not exist at character 232
database_dev  | 2023-05-26 13:38:01.598 UTC [83] STATEMENT:  SELECT "vault_api"."id", "vault_api"."name", "vault_api"."auth", "vault_api"."category_id", "vault_api"."cors", "vault_api"."description", "vault_api"."https", "vault_api"."url", "vault_api"."view_count", "vault_api"."source" FROM "vault_api" LIMIT 21
database_dev  | 2023-05-26 13:38:01.624 UTC [83] ERROR:  relation "vault_api" does not exist at character 232
```
or
```bash
server_dev    |   File "/usr/local/lib/python3.8/dist-packages/psycopg2/__init__.py", line 122, in connect
server_dev    |     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
server_dev    | psycopg2.OperationalError: connection to server at "database" (172.20.0.2), port 5432 failed: Connection refused
server_dev    |         Is the server running on that host and accepting TCP/IP connections?
```

To fix those erros just stop it and relaunch `docker-compose up`

**Note**:

Please open an [Issue](https://github.com/Exifly/ApiVault/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=) if you see docker errors! (You can try fix on your own if you want)

Now just go on **localhost:3000** on your browser.


### Done

<hr />

# Credits 

This software uses the following open source packages:

### Tools 🔧
- [GSAP](https://greensock.com/gsap/)
- [public-apis](https://github.com/public-apis/public-apis) (a portion of our data)

<hr />

# Contributing 

If you've ever wanted to contribute to open source, and a great cause, now is your chance!

> When contributing to this repository, please first discuss the change you wish to make via issues with the authors of this repository before making a change. <br>
> Make sure to go through the **[CODE OF CONDUCT](https://github.com/Exifly/ApiVault/blob/main/CODE_OF_CONDUCT.md)** once before making changes!

### How to Contribute 🤔

- Look at the existing [**Issues**](https://github.com/Exifly/ApiVault/issues) or [**create a new issue**](https://github.com/Exifly/ApiVault/issues/new/choose)!
- [**Fork the Repo**](https://github.com/Exifly/ApiVault/fork) to make changes. 
- Then, create a branch for any issue that you are working on. 
- Finally, implement your changes by committing your work.
- Create a **[Pull Request](https://github.com/Exifly/ApiVault/compare)** (_PR_), which will be promptly reviewed and given suggestions for improvements by the community.
- Add screenshots or screen captures to your Pull Request to help us understand the effects of the changes proposed in your PR.

> For more detailed instructions ---> **[CONTRIBUTING.md](https://github.com/Exifly/ApiVault/blob/main/CONTRIBUTING.md)**

## Contributors ✨

Thanks go to these wonderful people ✨:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/gdjohn4s"><img src="https://avatars.githubusercontent.com/u/19678157?v=4?s=100" width="100px;" alt="gdjohn4s"/><br /><sub><b>gdjohn4s</b></sub></a><br />🥳</td>
      <td align="center"><a href="https://github.com/FlavioAdamo"><img src="https://avatars.githubusercontent.com/u/46765573?v=4?s=100" width="100px;" alt="Flavio Adamo"/><br /><sub><b>Flavio Adamo</b></sub></a><br />🥳</td>
      <td align="center"><a href="https://github.com/NirajD10"><img src="https://avatars.githubusercontent.com/u/66014487?v=4" width="100px;" alt="NirajD10"/><br /><sub><b>NirajD10</b></sub></a><br />🥳</td>
      <td align="center"><a href="https://github.com/kiabq"><img src="https://avatars.githubusercontent.com/u/44178907?v=4" width="100px;" alt="kiabq"/><br /><sub><b>kiabq</b></sub></a><br />🥳</td>
      <td align="center"><a href="https://github.com/the-amazing-atharva"><img src="https://avatars.githubusercontent.com/u/121221252?v=4" width="100px;" alt="Atharva Salitri"/><br /><sub><b>Atharva Salitri</b></sub></a><br />🥳</td>
      <td align="center"><a href="https://github.com/caickPassarella"><img src="https://avatars.githubusercontent.com/u/25408543?v=4" width="100px;" alt="Caick"/><br /><sub><b>Caick</b></sub></a><br />🥳</td>
      <td align="center"><a href="https://github.com/kotkaravishkar"><img src="https://avatars.githubusercontent.com/u/94035734?v=4" width="100px;" alt="Avishkar Kotkar
"/><br /><sub><b>Avishkar Kotkar
</b></sub></a><br />🥳</td>
      <td align="center"><a href="https://github.com/iamjamesfrancis"><img src="https://avatars.githubusercontent.com/u/55175085?v=4" width="100px;" alt="James Francis
"/><br /><sub><b>James Francis
</b></sub></a><br />🥳</td>
      <td align="center"><a href="https://github.com/MOHDNEHALKHAN"><img src="https://avatars.githubusercontent.com/u/125626654?v=4" width="100px;" alt="MOHD NEHAL KHAN
"/><br /><sub><b>MOHD NEHAL
</b></sub></a><br />🥳</td>
      <td align="center"><a href="https://github.com/tarunsamanta2k20"><img src="https://avatars.githubusercontent.com/u/55488549?v=4" width="100px;" alt="Tarun Samanta"/><br /><sub><b>Tarun Samanta
</b></sub></a><br />🥳</td>
    </tr>
    <tr>
       <td align="center"><a href="https://github.com/realrohitgurav"><img src="https://avatars.githubusercontent.com/u/110970889?v=4" width="100px;" alt="Rohit Gurav"/><br /><sub><b>Rohit Gurav
</b></sub></a><br />🥳</td>
       <td align="center"><a href="https://github.com/Badrnyali"><img src="https://avatars.githubusercontent.com/u/71897147?v=4" width="100px;" alt="Badrnyali"/><br /><sub><b>Badrnyali
         </b></sub></a><br />🥳</td>
        <td align="center"><a href="https://github.com/gianmazzoran"><img src="https://avatars.githubusercontent.com/u/16735648?v=4" width="100px;" alt="bytemore"/><br /><sub><b>bytemore
      </b></sub></a><br />🥳</td>
        <td align="center"><a href="https://github.com/HassanTanveer"><img src="https://avatars.githubusercontent.com/u/57575219?v=4" width="100px;" alt="Hassan Tanveer"/><br /><sub><b>Hassan Tanveer
      </b></sub></a><br />🥳</td>
        <td align="center"><a href="https://github.com/cyberGHostJs"><img src="https://avatars.githubusercontent.com/u/105425922?v=4" width="100px;" alt="cyberGHostJs"/><br /><sub><b>cyberGHostJs
      </b></sub></a><br />🥳</td>
        <td align="center"><a href="https://github.com/et-c"><img src="https://avatars.githubusercontent.com/u/54663819?v=4" width="100px;" alt="et-c"/><br /><sub><b>et-c
      </b></sub></a><br />🥳</td>
        <td align="center"><a href="https://github.com/DomeT99"><img src="https://avatars.githubusercontent.com/u/85518808?v=4" width="100px;" alt="Domenico Tenace"/><br /><sub><b>Domenico Tenace
      </b></sub></a><br />🥳</td>
    </tr>
  </tbody>
</table>

## Support 
Feel free to open issues and pull requests and **Don't forget to leave a star ⭐**
If you want to support us with a coffee, that's how to do it! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/T6T0LL2YG)

## License 
ApiVault is licensed under the terms of **CC BY-NC-ND 4.0**. Check out [LICENSE](https://github.com/Exifly/ApiVault/blob/main/LICENSE) for details.

<br>

> [exifly.it](https://exifly.it) &nbsp;&middot;&nbsp;
> GitHub [@exifly](https://github.com/Exifly) &nbsp;
