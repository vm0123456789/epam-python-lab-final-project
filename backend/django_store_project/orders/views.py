from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from django.db.models.signals import pre_save, post_save

from .models import Order, OrderItem
from store.models import Game
from .permissions import isAdminOrReadOnly  # TODO
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import OrderItemSerializer, OrderSerializer

from rest_framework.response import Response


# class ListOrder(generics.ListCreateAPIView):
#     permission_classes = (IsAdminUser,)
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAdminUser,)
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# def add_to_cart(request, id):
#     game = get_object_or_404(Game, id=id)
#     order = Order.objects.filter(user=request.user, is_ordered=False)
#     if order.exists():
#         # check if the order item is in the order
#         if order.items.filter()

class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = Order.objects.filter(user=request.user, ordered=False).first()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        user = request.user
        order, _ = Order.objects.get_or_create(user=user, ordered=False)
        game = Game.objects.get(id=data.get('id'))
        qty = data.get('qty')
        if OrderItem.objects.filter(order=order, game=game).exists():
            return Response({'msg': 'Item already exists'}, status=status.HTTP_409_CONFLICT)
        order_item = OrderItem(game=game, qty=qty, order=order)
        order_item.save()
        return Response({'success': 'Item is added to the order'}, status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        order = Order.objects.filter(user=request.user, ordered=False).first()
        order_item = OrderItem.objects.filter(order=order, game=data.get('id')).first()
        qty = data.get('qty')
        order_item.qty = qty
        order_item.save()
        return Response({'success': 'Item is updated'}, status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.data
        order = Order.objects.filter(user=request.user, ordered=False).first()
        order_item = OrderItem.objects.filter(order=order, game=data.get('id'))
        order_item.delete()
        return Response({'success': 'Item is deleted from the order'}, status=status.HTTP_204_NO_CONTENT)

# @receiver(pre_save, sender=OrderItem)
# def correct_price(sender, **kwargs):
#     print('I got called')
