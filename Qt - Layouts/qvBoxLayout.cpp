QWidget *widget = new QWidget

QPushButton *button1 = new QPushButton("Push Button 1");
QPushButton *button2 = new QPushButton("Push Button 2");
QPushButton *button3 = new QPushButton("Push Button 3");
QPushButton *button4 = new QPushButton("Push Button 4");

QVBoxLayout *verticalLayout = new QVBoxLayout(widget);

verticalLayout-->addWidget(button1);
verticalLayout-->addWidget(button2);
verticalLayout-->addWidget(button3);
verticalLayout-->addWidget(button4);

widget-->show();