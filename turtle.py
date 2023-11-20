import turtle

# Создаем объект черепахи
t = turtle.Turtle()

# Устанавливаем скорость рисования
t.speed(2)

# Рисуем сердце
t.fillcolor("red")
t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()

# Скрываем черепаху
t.hideturtle()

# Закрываем окно при клике
turtle.exitonclick()
