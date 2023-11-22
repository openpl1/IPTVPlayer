
def getWidgetText(widgetPointer):
    try:
        return(widgetPointer.Text)
    except Exception:
        try:
            return(widgetPointer.textU)
        except Exception:
            return(widgetPointer.text)

def innerWidgetTextRight(widgetPointer):
    try:
        return(widgetPointer.innerright())
    except Exception:
        return(widgetPointer.innerRight())
