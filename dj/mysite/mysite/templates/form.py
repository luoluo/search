<html>
<head>
    <title>Contact us</title>
</head>
<body>
    <h1>Contact us</h1>

    {% if form.errors %}
        <p style="color: red;">
            Please correct the error{{ form.errors|pluralize }} below.
        </p>
    {% endif %}

    <form action="" method="post">{% csrf_token %} 
        <table>
            {{ form.as_table }}  #生成表单
        </table>
        <input type="submit" value="Submit">
    </form>
</body>
</htm
