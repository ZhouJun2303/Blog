---
id: MO1gKS
title: Cocos集成高德定位
createdAt: "2019-07-30 10:35:56"
updated: "2026-06-16 17:26:22"
tags:
    - Cocos
    - 定位
tag_ids:
    - Zuqsnn
    - N42Mim
categories: []
published: true
hideInList: false
feature: ""
isTop: false
---

Key
```
d7be719a0580ae65f050b3ec85e75f57  key
```
```
// Learn cc.Class:
//  - [Chinese] https://docs.cocos.com/creator/manual/zh/scripting/class.html
//  - [English] http://docs.cocos2d-x.org/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - [Chinese] https://docs.cocos.com/creator/manual/zh/scripting/reference/attributes.html
//  - [English] http://docs.cocos2d-x.org/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - [Chinese] https://docs.cocos.com/creator/manual/zh/scripting/life-cycle-callbacks.html
//  - [English] https://www.cocos2d-x.org/docs/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {
        // foo: {
        //     // ATTRIBUTES:
        //     default: null,        // The default value will be used only when the component attaching
        //                           // to a node for the first time
        //     type: cc.SpriteFrame, // optional, default is typeof default
        //     serializable: true,   // optional, default is true
        // },
        // bar: {
        //     get () {
        //         return this._bar;
        //     },
        //     set (value) {
        //         this._bar = value;
        //     }
        // },
    },

    // LIFE-CYCLE CALLBACKS:

    onLoad() {
        
    },

    getlocation(){
        var map = new AMap.Map('container', {
            resizeEnable: true, //是否监控地图容器尺寸变化
            zoom: 11, //初始化地图层级
            center: [116.397428, 39.90923] //初始化地图中心点
        });
        console.log(map);
        map.on("complete", function () {
            log.success("地图加载完成！");
        });

        //定位
        map.plugin('AMap.Geolocation', function () {
            var geolocation = new AMap.Geolocation({
                // 是否使用高精度定位，默认：true
                enableHighAccuracy: true,
                // 设置定位超时时间，默认：无穷大
                timeout: 10000,
                // 定位按钮的停靠位置的偏移量，默认：Pixel(10, 20)
                buttonOffset: new AMap.Pixel(10, 20),
                //  定位成功后调整地图视野范围使定位位置及精度范围视野内可见，默认：false
                zoomToAccuracy: true,
                //  定位按钮的排放位置,  RB表示右下
                buttonPosition: 'RB'
            })

            geolocation.getCurrentPosition()
            AMap.event.addListener(geolocation, 'complete', onComplete)
            AMap.event.addListener(geolocation, 'error', onError)

            function onComplete(data) {
                // data是具体的定位信息
                console.log("定位成功！");
                console.log(data);
            }

            function onError(data) {
                // 定位出错
                console.log("定位出错!");
                console.log(data);
            }
        })


        AMap.plugin('AMap.CitySearch', function () {
            var citySearch = new AMap.CitySearch()
            citySearch.getLocalCity(function (status, result) {
              if (status === 'complete' && result.info === 'OK') {
                // 查询成功，result即为当前所在城市信息
                console.log(result);
              }
            })
          })
    },




    //


    start() {
        this.getlocation();
    },

    // update (dt) {},
});
```
```
// Learn cc.Class:
//  - [Chinese] https://docs.cocos.com/creator/manual/zh/scripting/class.html
//  - [English] http://docs.cocos2d-x.org/creator/manual/en/scripting/class.html
// Learn Attribute:
//  - [Chinese] https://docs.cocos.com/creator/manual/zh/scripting/reference/attributes.html
//  - [English] http://docs.cocos2d-x.org/creator/manual/en/scripting/reference/attributes.html
// Learn life-cycle callbacks:
//  - [Chinese] https://docs.cocos.com/creator/manual/zh/scripting/life-cycle-callbacks.html
//  - [English] https://www.cocos2d-x.org/docs/creator/manual/en/scripting/life-cycle-callbacks.html

cc.Class({
    extends: cc.Component,

    properties: {
        // foo: {
        //     // ATTRIBUTES:
        //     default: null,        // The default value will be used only when the component attaching
        //                           // to a node for the first time
        //     type: cc.SpriteFrame, // optional, default is typeof default
        //     serializable: true,   // optional, default is true
        // },
        // bar: {
        //     get () {
        //         return this._bar;
        //     },
        //     set (value) {
        //         this._bar = value;
        //     }
        // },
    },

    // LIFE-CYCLE CALLBACKS:

    onLoad() {
        
    },

    getlocation(){
        var map = new AMap.Map('container', {
            resizeEnable: true, //是否监控地图容器尺寸变化
            zoom: 11, //初始化地图层级
            center: [116.397428, 39.90923] //初始化地图中心点
        });
        console.log(map);
        map.on("complete", function () {
            log.success("地图加载完成！");
        });

        //定位
        map.plugin('AMap.Geolocation', function () {
            var geolocation = new AMap.Geolocation({
                // 是否使用高精度定位，默认：true
                enableHighAccuracy: true,
                // 设置定位超时时间，默认：无穷大
                timeout: 10000,
                // 定位按钮的停靠位置的偏移量，默认：Pixel(10, 20)
                buttonOffset: new AMap.Pixel(10, 20),
                //  定位成功后调整地图视野范围使定位位置及精度范围视野内可见，默认：false
                zoomToAccuracy: true,
                //  定位按钮的排放位置,  RB表示右下
                buttonPosition: 'RB'
            })

            geolocation.getCurrentPosition()
            AMap.event.addListener(geolocation, 'complete', onComplete)
            AMap.event.addListener(geolocation, 'error', onError)

            // function onComplete(data) {
            //     // data是具体的定位信息
            //     console.log("定位成功！");
            //     console.log(data);
            // }

            // function onError(data) {
            //     // 定位出错
            //     console.log("定位出错!");
            //     console.log(data);
            // }
        })


        AMap.plugin('AMap.CitySearch', function () {
            var citySearch = new AMap.CitySearch()
            citySearch.getLocalCity(function (status, result) {
              if (status === 'complete' && result.info === 'OK') {
                // 查询成功，result即为当前所在城市信息
                console.log(result.city);
                console.log(result);
                console.log(result.bounds.kc);
              }
            })
          })
    },




    //搜索地名查出经纬度
   geoCode() {
        AMap.plugin('AMap.Geocoder', function() {
            var geocoder = new AMap.Geocoder({
                // city 指定进行编码查询的城市，支持传入城市名、adcode 和 citycode
            })
            // var address  = document.getElementById('tipinput').value;
            var address = '武汉';
            geocoder.getLocation(address, function(status, result) {
                if (status === 'complete' && result.info === 'OK') {
                    var lnglat = result.geocodes[0].location.toString();
                    var lnglatArray = lnglat.split(",");
                    $("#lonNum").val(lnglatArray[0]);
                    $("#latNum").val(lnglatArray[1]);
                    var map = new AMap.Map("container", {
                    });
                    var marker = new AMap.Marker({
                        icon: "//a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-red.png",
                        position: new AMap.LngLat(lnglatArray[0],lnglatArray[1]),   // 经纬度对象，也可以是经纬度构成的一维数组[116.39, 39.9]
                        offset: new AMap.Pixel(-13, -30)
                    });
                   
                    console.log(marker);
                    console.log(marker.bounds.kc);
                }
            })
     
        })
    },

    //搜索
    search(){
        AMap.plugin('AMap.Autocomplete', function(){
            // 实例化Autocomplete
            var autoOptions = {
              //city 限定城市，默认全国
              city: '全国'
            }
            var autoComplete= new AMap.Autocomplete(autoOptions);
            autoComplete.search('广州', function(status, result) {
              // 搜索成功时，result即是对应的匹配数据
              console.log("搜索成功");
              console.log(result);
              console.log(result.tips[0].location);
            })
          })
    },
    
   


    start() {
        this.getlocation();
        // this.geoCode();
        this.search();
    },

    // update (dt) {},
});
```