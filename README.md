# seumeduDriller
=========

산업안전교육이 귀찮아서 만듬    
전처럼 배포하거나하지 않고 혼자 써먹고 기록용도로만 남김    
keducenter때랑 비슷한걸로봐서 같은업체가 만든거같음    
대충 로그인후 세션아이디 넣어주고(헤더,쿠키)    


no는 학습커리큘럼에 관련된 번호라서 실제 오고가는 데이터를 까봐야 알수있음.    
num에 차시, log_num에 차시 내부에 페이지를 배열형태로(1,2,3,4,5,)     
cl_start_time과 cl_start_check로 학습시간체크를 하는줄알았는데, 그게 아니라서 timer.py를 따로만듬.    
이를 for문으로 해당차시의 log_num만큼 반복시키면 학습 프로세스 체크 100%를 달성시킬수있지만    
학습시간에는 10초 이렇게 나오니 cl_start_time을 늘려서 여러번 보내 학습시간을 늘릴수있게 한 timer.py를 따로 돌려줘야함.    
하나의 로직으로 합칠수도 있지만 한번쓰고 말것이 뻔하기때문에 매크로처럼 사용하고 이쯤에서 정리함.    


