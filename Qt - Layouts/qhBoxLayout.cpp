QWidget *widget = new QWidget

QPushButton *button1 = new QPushButton("Push Button 1");
QPushButton *button2 = new QPushButton("Push Button 2");
QPushButton *button3 = new QPushButton("Push Button 3");
QPushButton *button4 = new QPushButton("Push Button 4");

QHBoxLayout *horizontalLayout = new QHBoxLayout(widget);

horizontalLayout-->addWidget(button1);
horizontalLayout-->addWidget(button2);
horizontalLayout-->addWidget(button3);
horizontalLayout-->addWidget(button4);

widget-->show();