# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ![DEFRA Banner](files/images/DEFRA_branding/Banner_700x200_Building_a_greener_future.jpg)
# MAGIC
# MAGIC # Markdown Examples
# MAGIC <a name="Top"></a>
# MAGIC One of the main advantages of coding in a notebook is felaxbility in presentation.  
# MAGIC The output of each code cell is shown directly below that cell. 
# MAGIC This makes it easier to not only show what each section of code does but to tell a story. You can taylor the look of your notebook to your audience.  
# MAGIC For collaboration you can add markdown cells to explain code, thoughts, concepts or insights in a far more readable way that normal code comments. You can also include external links and images.
# MAGIC You can still use normal comments in your code as well.  
# MAGIC For a less technical audiance you can hide code cells.  
# MAGIC You can also include in-notebook links to jump to particular cells.  
# MAGIC   
# MAGIC This notebook contains several examples of markdown that you could use to prettify your own notebooks.
# MAGIC
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Switching a cell to markdown
# MAGIC To see how a cell will be interpreted, look above the right hand corner of the cell. There will be text indicating which language the cell uses.  To turn a cell into a markdown cell you can add "%md" to the first line in the cell. Or you can click on the text of the current language and select markdown from the drop down menu. This adds the "%md" for you.  
# MAGIC Running the cell, or clicking off it, will replace the markdown text with it's output.  
# MAGIC To edit a markdown cell double click it and it wil return to the markdown code.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Headings
# MAGIC To create a heading, add \# to the begining of the text.  
# MAGIC Sub-headings can be added with double or more hashes, reducing the size of font.  
# MAGIC eg.  
# MAGIC \# Heading
# MAGIC # Heading
# MAGIC \## Sub-heading
# MAGIC ## Sub-heading
# MAGIC First two levels will apear in the Data Explorer.  
# MAGIC   
# MAGIC \### Sub-Sub-heading
# MAGIC ### Sub-sub-heading
# MAGIC \#### Etc
# MAGIC #### Etc
# MAGIC
# MAGIC In addition, cells begining with the first two level of headings can be jumped to from the Data Explorer, the "Table of contents" icon. (just below File at the top of the notebook) 
# MAGIC HTML header tags can also be used for headings however these will not appear in the tabel of contents.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <h1>HTML Header</h1>
# MAGIC Not in table of contents

# COMMAND ----------

# MAGIC %md
# MAGIC ## Lines
# MAGIC To further break up a notebook into sections a line can be draw with three dashes or asterisks. \--- or \*** or the html tag \<hr>  
# MAGIC eg.  
# MAGIC ---
# MAGIC ***
# MAGIC <hr>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Text formatting and layout
# MAGIC The simplest use of a markdown cell would be text similar to how you would add a comment to code, but is a bit clearer to read.  
# MAGIC The text will not display exactly as written. Text with a carrage return will still run together. If you want to create a second paragraph, or a blank line, you can add a double space to the end of the line.  
# MAGIC   
# MAGIC Or you can use the html breakline tag. \<br> <br>
# MAGIC To be able to include markdown code in a markdown cell you put a \ in front of the instruction.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Text Emphasis
# MAGIC
# MAGIC  _Italics_ \_Italics_ or \*Italics*  
# MAGIC **Bold**  \_\_Bold__ or \*\*Bold**  
# MAGIC ***Bold and italics*** \_\_\_Bold and italics___ or \*\*\*Bold and italics\*\*\*  
# MAGIC ~StrikeThrough~ \~StrikeThrough~  
# MAGIC
# MAGIC >Block quotes \>Block quotes
# MAGIC >>Nested Block quotes \>\>Nested Block quotes
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Lists
# MAGIC
# MAGIC Bullet points  
# MAGIC
# MAGIC \* or \- then a space  
# MAGIC Two spaces at start of line for nested bullet points
# MAGIC * First &check;
# MAGIC * Second
# MAGIC   * Nested First &cross;
# MAGIC   * Nested Second
# MAGIC * Third
# MAGIC
# MAGIC Ticks can be added with \&check;  
# MAGIC Or crosses with \&cross;
# MAGIC
# MAGIC Ordered List, number then full stop, eg 1. at start of line.
# MAGIC 1. First
# MAGIC 2. Second
# MAGIC 3. Third

# COMMAND ----------

# MAGIC %md
# MAGIC ###  UTF-8 Geometric shapes
# MAGIC
# MAGIC As well as ticks and crosses there are other shapes that can be used.
# MAGIC
# MAGIC eg.  
# MAGIC &square; \&square;  
# MAGIC &triangle; \&triangle;  
# MAGIC &#9632; \&#9632;
# MAGIC
# MAGIC A list can be found here:
# MAGIC [](link UTF-8)

# COMMAND ----------

# MAGIC %md
# MAGIC ### KaTexX
# MAGIC
# MAGIC For displaying a mathimatical formula markdown can interprt KaTeX.  (Similar to Latex)
# MAGIC
# MAGIC eg.  
# MAGIC Bayes  
# MAGIC \\(P(A|B) = \frac{P(A|B)P(A)}{P} \\)
# MAGIC
# MAGIC Einstein  
# MAGIC \\(E = M C^2 \\)
# MAGIC
# MAGIC \\(c = \\pm\\sqrt{a^2 + b^2} \\)
# MAGIC
# MAGIC \\(A{_i}{_j}=B{_i}{_j}\\)
# MAGIC
# MAGIC $$c = \\pm\\sqrt{a^2 + b^2}$$
# MAGIC
# MAGIC \\[A{_i}{_j}=B{_i}{_j}\\]
# MAGIC
# MAGIC \\( f(\beta)= -Y_t^T X_t \beta + \sum log( 1+{e}^{X_t\bullet\beta}) + \frac{1}{2}\delta^t S_t^{-1}\delta\\)
# MAGIC
# MAGIC where \\(\delta=(\beta - \mu_{t-1})\\)
# MAGIC
# MAGIC
# MAGIC In darkmode the fraction line and square roots appear black, not sure why?

# COMMAND ----------

# MAGIC %md
# MAGIC ### Inline code
# MAGIC
# MAGIC `print(inline code)`  \`print(inline code)`
# MAGIC
# MAGIC ```
# MAGIC def my_function():
# MAGIC     print('Markdown is cool')
# MAGIC ```
# MAGIC \```  
# MAGIC def my_function():  
# MAGIC     print('Markdown is cool')  
# MAGIC \```

# COMMAND ----------

# MAGIC %md
# MAGIC ## Tables
# MAGIC
# MAGIC Tables can be rendered using pipes and dashes.  
# MAGIC You can uses spaces and more dashes to make the raw markdown easier to read/edit but they are not nessisary.  
# MAGIC Markdown tables align left by default. (This can usually be changed with a colon after the dash for right align or both before and after for centre align. However this dosen't appear to work in Databricks)  
# MAGIC   
# MAGIC Tables can contain markdown syntax.  
# MAGIC
# MAGIC | Column 1 | Column 2 |Column 3|
# MAGIC |----------|---------:|-|
# MAGIC | Row 1    | Row 1    |Row 1|
# MAGIC |_Row 2_   |**Row 2** |Row 2|
# MAGIC |Row 3|Row 3|Row 4|
# MAGIC
# MAGIC
# MAGIC Double click on this cell to see the raw table code.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Hyperlinks
# MAGIC
# MAGIC Clickable links can be included in markdown.

# COMMAND ----------

# MAGIC %md
# MAGIC ### External
# MAGIC
# MAGIC hyperlink format:  
# MAGIC \[Text on screen](url "Hover over text")
# MAGIC eg.  
# MAGIC [DEFRA](https://www.gov.uk/government/organisations/department-for-environment-food-rural-affairs "DEFRA website on gov.uk" )

# COMMAND ----------

# MAGIC %md
# MAGIC ## Images
# MAGIC
# MAGIC Images can be inserted into markdown cells.
# MAGIC Format:  
# MAGIC  \!\[Alt text](path/to/image.jpg "Hover over")  
# MAGIC  Alt text will be displayed if the file is not found.  
# MAGIC  Hover over will show when cursor idles on the image.  
# MAGIC
# MAGIC  eg.  
# MAGIC  ![You should been looking at penguins](files/images/penguins.jpg  "P-P-Pick up a...")
# MAGIC
# MAGIC  ![You should been looking at penguins](files/images/typo.jpg  "P-P-Pick up a...")
# MAGIC
# MAGIC  Tip: A banner style image can look good at the top of a notebook.
# MAGIC
# MAGIC  

# COMMAND ----------

# MAGIC %md
# MAGIC ## HTML
# MAGIC As you might have guessed by now some html can be used within markdown. Much of the above markdown code has an html equivalent but if you are familiar with HTML you can do a lot more.  
# MAGIC   
# MAGIC You can try the html and if it doesn't work you can try:  
# MAGIC displayHTML()  
# MAGIC in a code cell.
# MAGIC
# MAGIC Some examples that might be handy:
# MAGIC
# MAGIC Styled to look like a command prompt
# MAGIC <p style="background:black>
# MAGIC <code style="background:black;color:white;font-family:Consolas">C:\Users\rishi\
# MAGIC </code>
# MAGIC </p>
# MAGIC
# MAGIC

# COMMAND ----------

displayHTML("<h3>You can view HTML code in notebooks.</h3> ")

# COMMAND ----------


