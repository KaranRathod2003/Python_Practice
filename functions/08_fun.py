def functions_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
functions_kwargs(name="karan", surname="rathod")
functions_kwargs(name="hinal", surname="rathod")
functions_kwargs(name="yashwant", surname="rathod", father_name="ramchandra")