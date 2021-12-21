```
/* 입력된 날짜가 유효한지 확인하는 함수 */
/* 입력된 날짜(date)를 날짜 포맷(dateFormat)에 맞춰 자른 뒤 연월일시분초가 정확한 날짜인지 확인 */
/* 정상: return 1, 비정상: return 0 */
function checkDate(date, dateFormat) {
    /* -----날짜를 타입 별로 자르기 위한 인덱스----- */
    let yIdx = dateFormat.indexOf('y'); // 연 시작 인덱스
    let yLastIdx = dateFormat.lastIndexOf('y'); // 연 끝 인덱스
    let MIdx = dateFormat.indexOf('M'); // 월 시작 인덱스
    let MLastIdx = dateFormat.lastIndexOf('M'); // 월 끝 인덱스
    let dIdx = dateFormat.indexOf('d'); // 일 시작 인덱스
    let dLastIdx = dateFormat.lastIndexOf('d'); // 일 끝 인덱스
    let HIdx = dateFormat.indexOf('H'); // 시 시작 인덱스
    let HLastIdx = dateFormat.lastIndexOf('H'); // 시 끝 인덱스
    let mIdx = dateFormat.indexOf("m"); // 분 시작 인덱스
    let mLastIdx = dateFormat.lastIndexOf("m"); // 분 끝 인덱스
    let sIdx = dateFormat.indexOf('s'); // 초 시작 인덱스
    let sLastIdx = dateFormat.lastIndexOf('s'); // 초 끝 인덱스

    /* -----인덱스를 이용해 날짜 자르며 validation check----- */
    let year = Number(date.slice(yIdx, yLastIdx + 1));
    if (year !== '' && (0 > year)) { return 0; }
    let month = Number(date.slice(MIdx, MLastIdx + 1));
    if (month !== '' && (0 > month || month > 12)) { return 0; }
    let day = Number(date.slice(dIdx, dLastIdx + 1));
    let lastDay = new Date(year, month, 0);
    lastDay = lastDay.getDate();
    if (day !== '' && (0 > day || day > lastDay)) { return 0; }
    let hour = Number(date.slice(HIdx, HLastIdx + 1));
    if (hour !== '' && (0 > hour || hour > 60)) { return 0; }
    let minute = Number(date.slice(mIdx, mLastIdx + 1));
    if (minute !== '' && (0 > minute || minute > 60)) { return 0; }
    let second = Number(date.slice(sIdx, sLastIdx + 1));
    if (second !== '' && (0 > second || second > 60)) { return 0; }

    return 1;
}

/* 입력한 값이 패턴에 유효한지 확인하는 함수 */
/* 입력된 타입(type)에 따라 값(value)이 유효한지 확인 */
/* 정상: return true, 비정상: return false */
function checkPatternValidation(type, value) {
    /* -----정규식----- */
    const collectionNameRegex = /^[a-zA-Z][a-zA-Z0-9+.\-*$_+:@&=,\'!~;?!\.*]*$/;
    const analyzerFilterRegex = /^[a-z|A-Z|0-9]+$/;
    const kmaOptionRegex = /^[A-Za-z0-9+\-*+]*$/;
    const nameRegex = /^[가-힣a-zA-Z0-9]+$/;
    const idRegex = /^[a-zA-Z0-9][a-zA-Z0-9]*$/;
    const ipRegex = /^(1|2)?\d?\d([.](1|2)?\d?\d){3}$/;
    const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    const phoneRegex = /^[0-9]{3}[-]{1}[0-9]{3,4}[-]{1}[0-9]{4}$/;
    const urlRegex = /(^http[s]?):\/\/.+?$/;

    /* -----타입 체크----- */
    switch (type) {
        case "coll":
            return collectionNameRegex.test(value);
        case "analyzerFilter":
            return analyzerFilterRegex.test(value);
        case "kmaOption":
            return kmaOptionRegex.test(value);
        case "name":
            return nameRegex.test(value);
        case "id":
            return idRegex.test(value);
        case "ip":
            return ipRegex.test(value);
        case "email":
            return emailRegex.test(value);
        case "phone":
            return phoneRegex.test(value);
        case "url":
            return urlRegex.test(value);
        default:
            return false;
    }
}
```