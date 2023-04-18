<template>
  <link
    href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css"
    rel="stylesheet"
  />
  <div class="page-404">
    <div class="outer">
      <div class="middle">
        <div class="inner">
          <!--BEGIN CONTENT-->
          <div class="inner-circle">
            <i class="anim-rotate fa fa-gear"></i><span>500</span>
          </div>
          <span class="inner-status">Oops! Something went Wrong!!</span>
          <span class="inner-detail">
            Some asteroids destroyed your starship!
            <RouterLink class="btn btn-info mtl mt-3" to="/">
              <i class="fa fa-home"></i>&nbsp; Return home
            </RouterLink>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.clearfix:before,
.clearfix:after {
  display: table;
  content: " ";
}
.clearfix:after {
  clear: both;
}

.page-404 .outer {
  position: absolute;
  top: 0;
  display: table;
  width: 100%;
  height: 100%;
}
.page-404 .outer .middle {
  display: table-cell;
  vertical-align: middle;
}
.page-404 .outer .middle .inner {
  width: 300px;
  margin-right: auto;
  margin-left: auto;
}
.page-404 .outer .middle .inner .inner-circle {
  height: 300px;
  border-radius: 50%;
  background-color: var(--bg-color);
}
.page-404 .outer .middle .inner .inner-circle:hover i {
  color: #39bbdb !important;
  background-color: #f5f5f5;
  box-shadow: 0 0 0 15px #39bbdb;
}
.page-404 .outer .middle .inner .inner-circle:hover span {
  color: #39bbdb;
}
.page-404 .outer .middle .inner .inner-circle i {
  font-size: 5em;
  line-height: 1em;
  float: right;
  width: 1.6em;
  height: 1.6em;
  margin-top: -0.7em;
  margin-right: -0.5em;
  padding: 20px;
  -webkit-transition: all 0.4s;
  transition: all 0.4s;
  text-align: center;
  color: #f5f5f5 !important;
  border-radius: 50%;
  background-color: #39bbdb;
  box-shadow: 0 0 0 15px #f0f0f0;
}
.page-404 .outer .middle .inner .inner-circle span {
  font-size: 11em;
  font-weight: 700;
  line-height: 1.2em;
  display: block;
  -webkit-transition: all 0.4s;
  transition: all 0.4s;
  text-align: center;
  color: #e0e0e0;
}
.page-404 .outer .middle .inner .inner-status {
  font-size: 20px;
  display: block;
  margin-top: 20px;
  margin-bottom: 5px;
  text-align: center;
  color: #39bbdb;
}
.page-404 .outer .middle .inner .inner-detail {
  line-height: 1.4em;
  display: block;
  margin-bottom: 10px;
  text-align: center;
  color: #999999;
}

.anim-rotate {
  animation: loading 1.5s linear infinite;
}

@keyframes loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
