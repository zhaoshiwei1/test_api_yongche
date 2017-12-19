# -*- coding: UTF-8 -*-
# some alternative function, if cannot directly render the web elements
class utility:

    def make_text_form(self, num):
        form_string = """"""
        form_string += """<div class="row uniform">"""
        for i in range(int(num)):
            form_string += """
            <div class="6u 12u$(xsmall)">
			    <label for="parameter">参数"""
            form_string += str(i+1) +""": """+""" </label>
			</div>
			<div class="6u$ 12u$(xsmall)">
				<input type="text" name = """+ "\"" + str(i+1) +"\"" +""" value=""/>
			</div>
            """
        form_string += """
        </div>
        """

        return form_string