### 사용설명서
### 1. 가상환경 설정
> conda env create -f conda_requirements.txt

### 2. run.py 실행
> python run.py -c "color_name" -b "background_color_name"

- color_name :<b> 'red', 'cyan', 'teal', 'lightgreen', 'blue', 'amber', 'pink', 'purple', 'yellow'</b> 택1
  <i>(default = 'blue')</i>
- background_color_name :<b> 'dark', 'light' </b>택 1 <i>(default = 'dark')</i>
  ex) python run.py -c blue -b dark 
