QWidget *widget = new QWidget

QPushButton *button1 = new QPushButton("Push Button 1");
QPushButton *button2 = new QPushButton("Push Button 2");
QPushButton *button3 = new QPushButton("Push Button 3");
QPushButton *button4 = new QPushButton("Push Button 4");

QGridLayout *gridLayout = new QGridLayout(widget);

gridLayout-->addWidget(button1);
gridLayout-->addWidget(button2);
gridLayout-->addWidget(button3);
gridLayout-->addWidget(button4);

widget-->show();