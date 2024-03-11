import 'dart:math';

import 'package:daphila/utils/const.dart';
import 'package:flutter/material.dart';
import 'package:flutter_card_swiper/flutter_card_swiper.dart';

class Dashboard extends StatefulWidget {
  const Dashboard({super.key});

  @override
  State<Dashboard> createState() => _DashboardState();
}

class _DashboardState extends State<Dashboard> {
  List<Container> cards = [
    Container(
      alignment: Alignment.center,
      child: const Text('1'),
      color: Colors.blue,
    ),
    Container(
      alignment: Alignment.center,
      child: const Text('2'),
      color: Colors.red,
    ),
    Container(
      alignment: Alignment.center,
      child: const Text('3'),
      color: Colors.purple,
    )
  ];

  @override
  Widget build(BuildContext context) {
    double h = MediaQuery.of(context).size.height;
    double w = MediaQuery.of(context).size.width;
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              SizedBox(
                height: h * 0.01,
              ),
              SizedBox(child: logo),
              SizedBox(
                height: h / 1.5,
                width: double.infinity,
                child: CardSwiper(
                  scale: 0.9,
                  cardsCount: cards.length,
                  cardBuilder:
                      (context, index, percentThresholdX, percentThresholdY) =>
                          cards[index],
                  onSwipe: (previousIndex, currentIndex, direction) {
                    if (direction == CardSwiperDirection.left) {
                      debugPrint('YEs');
                      swipeNoti(context, 'You Swiped Left');
                    } else if (direction == CardSwiperDirection.right) {
                      swipeNoti(context, 'You Swiped Right');
                    } else if (direction == CardSwiperDirection.top) {
                      swipeNoti(context, 'You Swiped Up');
                    } else {
                      swipeNoti(context, 'You Swiped Bottom');
                    }
                    return true;
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future<String?> swipeNoti(BuildContext context, String message) {
    return showDialog<String>(
        context: context,
        builder: (BuildContext context) => Dialog(
                child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Text(message),
                  const SizedBox(height: 15),
                  TextButton(
                    onPressed: () {
                      Navigator.pop(context);
                    },
                    child: const Text('Close'),
                  ),
                ],
              ),
            )));
  }
}
