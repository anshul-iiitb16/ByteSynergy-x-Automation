import WebCode.lenoxex as website1
import WebCode.irisjobs as website2
import WebCode.newagesys as website3
import build1.gui as GUI
import build_resume.gui as GUI2


GUI.Start()

if(GUI.info == []):
	GUI2.Start()
	info = GUI2.info
	
else:
	info = GUI.info

# website1.web(info)
# website2.web()
# website3.web()

# scrap.begin()


