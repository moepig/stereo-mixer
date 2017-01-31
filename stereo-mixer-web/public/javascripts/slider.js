function sliderSetup(win, doc) {

    "use strict";

    var slider = doc.getElementById("range-ch1");
    var elm = doc.getElementById("showRangeArea");
    var view = new View();

    slider.addEventListener("input", function() {
        // ドラッグ中のイベント
        view.setTextValue(this.value);
    }, false);

    slider.addEventListener("change", function() {
        // マウスアップした際のイベント
        view.setTextValue(this.value);
    }, false);

    function View(){

        _sliderInit();

        function _sliderInit() {
            var vol = getVolume();
            setTextValue(vol);
            slider.value = vol;
        }

        function setTextValue(value) {
            elm.innerText = value - 0;
        }

        function getVolume() {
            // ここは実際の値を読むように作る
            return elm.innerText - 0;
        }

        return {
            setTextValue: setTextValue,
            getVolume: getVolume,
        };
    }

}

// DOM を読み込み終わったらセットアップ開始
$(document).ready(function(){
    sliderSetup(this, document);
});