{% extends "base.html" %}

{% block page_title %} Main page {% endblock %}


{% block content %}
 <<div style="margin: 0 auto;width: 400px ; height:300px ;
    border-radius: 15px;background-color: bisque; padding:20px; text-align:center; margin-top: 50px">
    <div class="form">
        <form  method="POST" enctype="multipart/form-data">
            <label>Please type your new answer </label><br>
            <textarea type="text" name='message'></textarea><br><br>
            <input type="file" name="image"><br><br>
            <button type="submit">Save new answer</button><br><br>
        </form>
    </div>
{% endblock %}