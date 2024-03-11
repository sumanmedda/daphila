import 'package:daphila/utils/custom_button.dart';
import 'package:flutter/material.dart';

var dppurple = const Color.fromARGB(255, 119, 33, 134);
var dpwhite = const Color.fromARGB(255, 249, 249, 249);

var logo = Row(
  children: [
    Text('DA', style: TextStyle(color: dpwhite, fontWeight: FontWeight.bold)),
    Text('PHILO',
        style: TextStyle(
            color: dppurple, fontWeight: FontWeight.bold, fontSize: 17))
  ],
);
