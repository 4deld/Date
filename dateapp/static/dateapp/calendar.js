const today = new Date();
    const setCalendarData = (year, month) => { // 둘 다 인간이 생각하는,,
      let calHtml = "";
      const setDate = new Date(year, month - 1, 1); //컴퓨터는 1 빼서 생각해서 month에서 1을 빼준다
      const firstDay = setDate.getDate();//getDate(): Get the day as a number (1-31) //이번 달의 첫째 날을 구한다
      const firstDayName = setDate.getDay(); //getDay(): Get the weekday as a number (0-6) //이번 달의 처음 요일을 구한다 0- 일요일
      //Date객체의 day 인자에 0을 넘기면 지난달의 마지막 날
      const lastDay = new Date( //이번 달의 마지막 날
        today.getFullYear(),
        today.getMonth() + 1,
        0
      ).getDate();
      const prevLastDay = new Date( //지난 달의 마지막 날
        today.getFullYear(),
        today.getMonth(),
        0
      ).getDate();


      //매월 일수가 달라지므로 이번 달 날짜 개수를 세기 위한 변수
      let startDayCount = 1;
      let lastDayCount = 1;

      //1~6주차 6번
      for (let i = 0; i < 6; i++) {
        //일요일~토요일 7번
        for (let j = 0; j < 7; j++) {
          // i == 0: 1주차
          // j < firstDayName: 이번 달 시작 요일 이전 일 때
          if (i == 0 && j < firstDayName) {
            if (j == 0) { //일요일
              calHtml +=
                `<div style='background-color:#FFB3BB;' class='calendar__day horizontalGutter'><span>${(prevLastDay - (firstDayName - 1) + j)}</span><span></span></div>`;
            } else if (j == 6) { //토요일
              calHtml +=
                `<div style='background-color:#FFB3BB;' class='calendar__day'><span>${(prevLastDay - (firstDayName - 1) + j)}</span><span></span></div>`;
            } else {  //나머지요일
              calHtml +=
                `<div style='background-color:#FFB3BB;' class='calendar__day horizontalGutter'><span>${(prevLastDay - (firstDayName - 1) + j)}</span><span></span></div>`;
            }
          }
          else if (i == 0 && j == firstDayName) {// j == firstDayName: 이번 달 시작 요일일 때
            if (j == 0) {
              calHtml +=
                `<a href="{% url 'dateapp:detail' %}" style='background-color:#FFE0BB;' class='calendar__day horizontalGutter'><span>${startDayCount}</span><span id='${year}-${month}-${setFixDayCount(startDayCount++)}'></span></a>`;
            } else if (j == 6) {
              calHtml +=
                `<a href="{% url 'dateapp:detail' %}" style='background-color:#FFE0BB;' class='calendar__day'><span>${startDayCount}</span><span id='${year}-${month}-${setFixDayCount(startDayCount++)}'></span></a>`;
            } else { 
              calHtml +=
                `<a href="{% url 'dateapp:detail' %}" style='background-color:#FFE0BB;' class='calendar__day horizontalGutter'><span>${startDayCount}</span><span id='${year}-${month}-${setFixDayCount(startDayCount++)}'></span></a>`;
            }
          }
          else if (i == 0 && j > firstDayName) { // j > firstDayName: 이번 달 시작 요일 이후 일 때
            if (j == 0) {
              calHtml +=
                `<a href="{% url 'dateapp:detail' %}" style='background-color:#FFFFBB' class='calendar__day horizontalGutter'><span>${startDayCount}</span><span id='${year}-${month}-${setFixDayCount(startDayCount++)}'></span></a>`;
            } else if (j == 6) {
              calHtml +=
                `<a href="{% url 'dateapp:detail' %}" style='background-color:#FFFFBB' class='calendar__day'><span>${startDayCount}</span><span id='${year}-${month}-${setFixDayCount(startDayCount++)}'></span></a>`;
            } else {
              calHtml +=
                `<a href="{% url 'dateapp:detail' %}" style='background-color:#FFFFBB' class='calendar__day horizontalGutter'><span>${startDayCount}</span><span id='${year}-${month}-${setFixDayCount(startDayCount++)}'></span></a>`;
            }
          }
          else if (i > 0 && startDayCount <= lastDay) { // startDayCount <= lastDay: 이번 달의 마지막 날이거나 이전일 때
            if (j == 0) {
              calHtml +=
                `<a href="{% url 'dateapp:detail' %}" style='background-color:#BBFFC9;'class='calendar__day horizontalGutter verticalGutter'><span>${startDayCount}</span><span id='${year}-${month}-${setFixDayCount(startDayCount++)}'></span></a>`;
            } else if (j == 6) {
              calHtml +=
                `<a href="{% url 'dateapp:detail' %}" style='background-color:#BBFFC9;'class='calendar__day verticalGutter'><span>${startDayCount}</span><span id='${year}-${month}-${setFixDayCount(startDayCount++)}'></span></a>`;
            } else {
              calHtml +=
                `<a href="{% url 'dateapp:detail' %}" style='background-color:#BBFFC9;'class='calendar__day horizontalGutter verticalGutter'><span>${startDayCount}</span><span id='${year}-${month}-${setFixDayCount(startDayCount++)}'></span></a>`;
            }
          }
          else if (startDayCount > lastDay) { // startDayCount > lastDay: 이번 달의 마지막 날 이후일 때
            if (j == 0) {
              calHtml +=
                `<div style='background-color:#B9E1FF;' class='calendar__day horizontalGutter verticalGutter'><span>${lastDayCount++}</span><span></span></div>`;
            } else if (j == 6) {
              calHtml +=
                `<div style='background-color:#B9E1FF;' class='calendar__day verticalGutter'><span>${lastDayCount++}</span><span></span></div>`;
            } else {
              calHtml +=
                `<div style='background-color:#B9E1FF;' class='calendar__day horizontalGutter verticalGutter'><span>${lastDayCount++}</span><span></span></div>`;
            }
          }
        }
      }
      document
        .querySelector("#calendar")
        .insertAdjacentHTML("beforeend", calHtml);
    };

    const setFixDayCount = number => { //캘린더 하루마다 아이디 부여
      let fixNum = "";
      if (number < 10) {
        fixNum = "0" + number;
      } else {
        fixNum = number;
      }
      return fixNum;
    };

    if (today.getMonth() + 1 < 10) {
      setCalendarData(today.getFullYear(), "0" + (today.getMonth() + 1)); //20200911
    } else {
      setCalendarData(today.getFullYear(), "" + (today.getMonth() + 1)); //20201011
    }