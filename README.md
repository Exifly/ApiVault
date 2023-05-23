<h1 align="center">
    <img src="https://raw.githubusercontent.com/Exifly/ApiVault/main/frontend/public/img/apivault-full-dark-nobg.png#gh-dark-mode-only" alt="apivault dark" width="200">
    <img src="https://raw.githubusercontent.com/Exifly/ApiVault/main/frontend/public/img/apivault-full-light-nobg.png#gh-light-mode-only" alt="ApiVault" width="200">
  <br>
</h1>

![screenshot](./assets/Hero.png)

<p align="center">
    <a href="https://github.com/Exifly/ApiVault/tree/main" alt="Stable">
        <img src="https://img.shields.io/badge/stable-1.4.0-green?style=for-the-badge" /></a>
    <a href="https://github.com/Exifly/ApiVault/tree/beta_v2.0.0-b1" alt="Beta">
        <img src="https://img.shields.io/badge/beta-2.0.0-blue?style=for-the-badge" /></a>
    <a href="https://github.com/exifly/apivault/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/exifly/apivault?style=for-the-badge" /></a>
    <a href="https://github.com/exifly/apivault/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/exifly/apivault?style=for-the-badge" /></a>
    <a href="https://github.com/exifly/apivault/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/actions/workflow/status/exifly/apivault/node.js.yml?style=for-the-badge" /></a><br>
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
  [![Vue.js](https://img.shields.io/badge/nuxt.js-35495E?style=for-the-badge&logo=nuxtdotjs&logoColor=4FC08D)](http://electron.atom.io/)
  [![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)](http://electron.atom.io/)
[![Flask](https://img.shields.io/badge/Django-000000?style=for-the-badge&logo=django&logoColor=white)](https://flask.palletsprojects.com/en/2.2.x/)




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
cat .env.sample > .env
```
## Client/Server side using Docker
```bash
# Go into the root folder
cd ApiVault

# Run docker
docker-compose up
```

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

We would love to have you, feel free to open issues and pull requests and **Don't forget to leave a star ⭐**

<a href="https://www.buymeacoffee.com/exifly" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## License 
ApiVault is licensed under the terms of **MIT License**. Check out [LICENSE](https://github.com/Exifly/ApiVault/blob/main/LICENSE) for details.

<br>

> [exifly.it](https://exifly.it) &nbsp;&middot;&nbsp;
> GitHub [@exifly](https://github.com/Exifly) &nbsp;
