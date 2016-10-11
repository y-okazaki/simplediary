from simplediary import app

@app.template_filter()
def date_jp(date):
    change_date = date.strftime('%Y年%m月%d日')
    return change_date

@app.template_filter()
def date_slash(date):
    change_date = date.strftime('%Y/%m/%d')
    return change_date
