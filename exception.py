def fun(l):
    try:
        c=(l[0]+l[1])/(l[2]-l[3])
        print(c)
    except  ArithmeticError as e:
        print("an error occured:",e)
    except LookupError as e:
        print("an error occured:",e)
    except Exception as e:
        print("an error occured:",e)
    finally:
        print("error handled")
l=[1,2,3,"g"]
fun(l)