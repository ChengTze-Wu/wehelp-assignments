class JsonData {
    getJson(url) {
        return new Promise((resolve, reject) => {
            // 建構一個 XMLHttpRequest 物件
            let xhr = new XMLHttpRequest();
            // open 設定請求
            xhr.open("GET", url, true);
            xhr.onload = function () {
                if (200 <= xhr.status && xhr.status <= 299) {
                    resolve(JSON.parse(xhr.responseText)["result"]["results"]);
                } else {
                    reject(`Error:${xhr.status}`);
                }
            };
            xhr.send();
        });
    }

    analyzeData(data) {
        // 景點名稱
        let stitle = data["stitle"];
        // 第一張圖檔網址
        let files = data["file"].toLowerCase();
        let img = files.slice(0, files.indexOf(".jpg") + 4);
        return [stitle, img];
    }
}
