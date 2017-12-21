# -*- coding: UTF-8 -*-
# some alternative function, if cannot directly render the web elements
class utility:

    def make_text_form(self, num):
        form_string = """"""
        form_string += """<div class="row uniform">"""
        for i in range(int(num)):
            form_string += """
            <div class="6u 12u$(xsmall)">
			    <label for="parameter">参数名"""
            form_string += str(i+1) +""" : """+""" </label>
			</div>
			<div class="6u$ 12u$(xsmall)">
				<input type="text" name = """+ "\"" + str(i+1) +"\"" +""" value=""/>
			</div>
            """
        form_string += """
        </div>
        """

        return form_string


    def make_category_form(self, category_dic):
        form_string = """"""
        form_string += """
            <div class="row uniform">
                <div class="6u 12u$(xsmall)">
                    <div class="select-wrapper">
                        <select name="category_id" id="">
						    <option value="">- Category -</option>"""
        for item in category_dic:
            form_string += """<option value="""+"\""+ str(item) +"\"" +""">""" + category_dic[item] + """</option>"""

        form_string += """
        				</select>
					</div>
				</div>
				<div class="6u$ 12u$(xsmall)">
                    <button name = "filter_tc" type = "submit" value="" class = "button fit small">Filter</button>
				</div>
			</div>
            """
        return form_string
